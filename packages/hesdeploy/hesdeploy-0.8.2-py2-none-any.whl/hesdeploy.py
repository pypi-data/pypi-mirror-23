#!/usr/bin/env python

import boto3
from botocore.exceptions import ClientError

import fnmatch
import re
import argparse
import base64
import os
import zipfile
import time
import sys

import deployConfig
from datetime import datetime
from hesburgh import heslog, hesutil

timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
deployDir = "deploy_%s" % timestamp

########### WALK
def walk(filefolder):
  toSearch = filefolder if type(filefolder) is str else filefolder.get("")

  if os.path.isfile(filefolder):
    realPath = filefolder
    yield realPath, os.path.basename(realPath)
  elif os.path.isdir(filefolder):
    for root, dirs, files in os.walk(filefolder, followlinks=True):
      for file in files:
        realPath = os.path.join(root, file)
        yield realPath, file
  else:
    heslog.error("Trying to walk %s that is neither file nor folder" % filefolder)

########### ZIP
def zipDir(zipf, toZip):
  for realPath, filename in walk(toZip):
    archivePath = os.path.relpath(realPath, '..')
    heslog.verbose("%s => %s" % (realPath, archivePath))
    zipf.write(realPath, archivePath)


def makeZip(zipName, paths):
  zipf = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED)
  heslog.verbose("Make zip %s" % zipName)
  for path in paths:
    zipDir(zipf, path)
  zipf.close()


############ LIFECYCLE
class Abort(Exception):
  pass

class Lifecycle(object):
  def __init__(self, args, config, timer):
    self.args = args
    self.config = config
    self.timer = timer
    self.deployFailure = False

    self.encrypted = {}


  # Used to check if any of the specified "exitOn" args were passed in as cli args
  def _check(self, name, *exitOn):
    for e in exitOn:
      if vars(self.args).get(e):
        heslog.info("Skipping %s because '%s' was specified" % (name, e))
        return False
    return True


  def _encrypt(self, kmsKey, key, val):
    if kmsKey and key not in self.encrypted:
      try:
        heslog.verbose("Encrypting %s" % key)

        client = boto3.client('kms')
        response = client.encrypt(
          KeyId=kmsKey,
          Plaintext=val,
        )
        self.encrypted[key] = base64.b64encode(response.get("CiphertextBlob")).decode("utf-8")
      except Exception as e:
        heslog.error(e)
        raise Abort("Encryption Error")

    elif key not in self.encrypted:
      self.encrypted[key] = val

    return self.encrypted[key]


  def _updateLambda(self, func, env, kmsKey):
    heslog.info("Updating lambda '%s'" % func)

    env = { k: self._encrypt(kmsKey, k, v) for k,v in env.iteritems() }

    try:
      client = boto3.client('lambda')
      # Get the current environment so we don't lose things we're not overwriting
      response = client.get_function_configuration(FunctionName=func)
      currentEnv = response.get("Environment", {}).get("Variables", {})
      currentEnv.update(env)
      heslog.debug(currentEnv)

      response = client.update_function_configuration(
        FunctionName=func,
        Environment={
          'Variables': currentEnv
        },
      )
    except ClientError as e:
      heslog.error(e)


  def _deployGateway(self, gatewayInfo):
    gateway = gatewayInfo.get("name")
    stackName = gatewayInfo.get("stack")
    heslog.info("Deploying Gateway from Stack: %s Name: %s" % (stackName, gateway))

    try:
      client = boto3.client("cloudformation")
      response = client.describe_stacks(
        StackName=stackName
      )

      outputs = response.get("Stacks")[0].get("Outputs", {})
      for i in outputs:
        if i.get("OutputKey", "") == gateway:
          apiId = i.get("OutputValue")
          break

      if not apiId:
        heslog.error("Gateway %s could not be found in outputs of %s" (gateway, stackName))
        return

      description = "Hesdeploy %s" % (self.config.deployFolder() if not self.args.envOnly else "envOnly")

      client = boto3.client("apigateway")
      client.create_deployment(
        restApiId=apiId,
        stageName=self.args.stage,
        description=description
      )
    except Exception as e:
      heslog.error(e)


  def preDeploy(self):
    heslog.addContext(stage="preDeploy")

    if self._check("template validation", "noAws"):
      file = "_"
      try:
        heslog.info("Validating Templates")
        client = boto3.client("cloudformation")
        for file in self.config.artifactTemplates():
          heslog.verbose("Validating %s" % file)
          with open(file) as f:
            response = client.validate_template(TemplateBody=f.read())
            self.config.setTemplateCapabilities(file, response.get("Capabilities", []))
      except Exception as e:
        heslog.error(e)
        raise Abort("Validation Failure on %s" % file)

    if self._check("artifact creation", "noPublish"):
      if self.config.artifactZips():
        os.mkdir(deployDir)


  def package(self):
    heslog.addContext(stage="package")
    heslog.info("Creating artifacts")

    for zipConf in self.config.artifactZips():
      makeZip("%s/%s.zip" % (deployDir, zipConf.get("Name")), zipConf.get("Files"))
    heslog.info("Finished zipping in %ss" % (self.timer.step(True)))


  def publish(self):
    heslog.addContext(stage="publish")
    try:
      if self._check("publishing files", "noAws"):
        client = boto3.client('s3')
        heslog.info("Publishing to s3://%s/%s" % (self.args.deployBucket, self.config.deployFolder()))

        heslog.info("Uploading config file")
        heslog.verbose("Upload %s => s3://%s/%s/%s" % (self.config.filename, self.args.deployBucket, self.config.deployFolder(), self.config.filename))
        client.upload_file(self.config.filename, self.args.deployBucket, '%s/%s' % (self.config.deployFolder(), self.config.filename))

        heslog.info("Uploading artifact templates")
        for file in self.config.artifactTemplates():
          heslog.verbose("Upload %s => s3://%s/%s/%s" % (file, self.args.deployBucket, self.config.deployFolder(), file))
          client.upload_file(file, self.args.deployBucket, '%s/%s' % (self.config.deployFolder(), file))

        if os.path.exists(deployDir):
          heslog.info("Uploading artifact zips")
          for realPath, filename in walk(deployDir):
            heslog.verbose("Upload %s => s3://%s/%s/%s" % (realPath, self.args.deployBucket, self.config.deployFolder(), filename))
            client.upload_file(realPath, self.args.deployBucket, '%s/%s' % (self.config.deployFolder(), filename))

        heslog.info("Finished publishing in %ss" % (self.timer.step(True)))
    except Exception as e:
      heslog.error(e)
      raise Abort("Publish Error")


  def createOrUpdate(self, stackConfig):
    stackName = stackConfig.get("name")
    path = self.config.deployFolder()
    template = stackConfig.get("template")
    rootTemplate = "https://s3.amazonaws.com/%s/%s/%s" % (self.args.deployBucket, path, template)

    params = [ { "ParameterKey": k, "ParameterValue": v } for k,v in stackConfig.get("params").iteritems() ]
    tags = [ { "Key": k, "Value": v } for k,v in stackConfig.get("tags").iteritems() ]

    stackArgs = {
      "StackName": stackName,
      "TemplateURL": rootTemplate,
      "Parameters": params,
      "Capabilities": stackConfig.get("capabilities"),
      "Tags": tags,
    }
    created = False

    heslog.verbose("Stack args %s" % stackArgs)

    if self._check("running cloudformation for %s" % template, "noAws", "publishOnly"):
      try:
        client = boto3.client('cloudformation')
        response = client.describe_stacks(
          StackName=stackName
        )
        created = True
      except ClientError:
        heslog.verbose("Stack %s does not exist" % (stackName))

      try:
        if created:
          heslog.addContext(stage="updateStack")
          heslog.info("Updating Stack '%s' with %s" % (stackName, template))
          response = client.update_stack(**stackArgs)
          waiterId = 'stack_update_complete'
          self.waitUpdate(response.get("StackId"))
        else:
          heslog.addContext(stage="createStack")
          heslog.info("Creating Stack '%s' with %s" % (stackName, template))
          response = client.create_stack(**stackArgs)
          waiterId = 'stack_create_complete'
          self.waitCreate(response.get("StackId"))
      except ClientError as e:
        heslog.error(e)
        self.deployFailure = True

      heslog.info("CF Finished in %ss" % (self.timer.step(True)))


  def postDeploy(self):
    heslog.addContext(stage="postDeploy")

    if (self._check("lambda update", "noAws", "publishOnly")
        and len(self.config.lambdaVars()) > 0
        and not self.deployFailure):
      for lambdaConf in self.config.lambdaVars():
        self._updateLambda(lambdaConf.get("name"), lambdaConf.get("vars", {}), lambdaConf.get("key"))
      heslog.info("Finished Updating Lambdas in %ss" % (self.timer.step(True)))

    if (self._check("api deploy", "noAws", "publishOnly")
        and not self.deployFailure
        and len(self.config.gateways) > 0):
      for gatewayInfo in self.config.gateways:
        self._deployGateway(gatewayInfo)
      heslog.info("Finshed Deploying Gateways in %ss" % (self.timer.step(True)))

    # remove temp directory
    if self._check("delete local artifacts", "keepLocal") and os.path.exists(deployDir):
      for root, dirs, files in os.walk(deployDir):
        for file in files:
          heslog.verbose("Removing tmp file %s/%s" % (root, file))
          os.remove(os.path.join(root, file))
      heslog.verbose("Removing tmp dir %s" % deployDir)
      os.rmdir(deployDir)


  def deleteStack(self, stackConfig):
    heslog.addContext(stage="deleteStack")
    client = boto3.client('cloudformation')
    stackName = stackConfig.get("name")
    stackId = None

    try:
      client = boto3.client('cloudformation')
      response = client.describe_stacks(
        StackName=stackName
      )
      stackId = response.get("Stacks", [])[0].get("StackId")
    except Exception as e:
      raise Abort(e)


    if self._check("stack delete", "noAws"):
      heslog.info("Deleting stack %s" % stackName)
      response = client.delete_stack(
        StackName=stackName,
      )

      self.waitDelete(stackId)
      heslog.info("Deleted stack in %s" % (self.timer.step(True)))


  def run(self):
    try:
      pattern = re.compile("^[a-zA-Z0-9]*$")
      if not pattern.match(self.args.stage):
        heslog.error("For the safety of any templates it is passed to, 'stage' must only contain alpha-numeric characters")
        raise Abort("Paramter Validation")

      if not self.args.noAws and not hesutil.getEnv("AWS_ROLE_ARN"):
        heslog.error("When 'noAws' has not been specified you must assume a role to run this script")
        return

      if self.args.noPublish and not self.args.deployFolder:
        heslog.error("When specifying 'noPublish' you must also specify 'deployFolder'")
        return

      if self.args.delete:
        for stackConfig in self.config.stacks():
          self.deleteStack(stackConfig)
        return

      if self._check("publish and deploy", "envOnly"):
        self.preDeploy()

        if self._check("publish steps", "noPublish"):
          self.package()
          self.publish()

        heslog.debug(self.config.stacks())
        if self._check("cloudformation", "publishOnly", "envOnly"):
          for stackConfig in self.config.stacks():
            if self.deployFailure:
              heslog.warn("Breaking due to DeployFailure")
              break
            self.createOrUpdate(stackConfig)

      self.postDeploy()
    except (Abort, ClientError) as e:
      heslog.setContext({})
      heslog.info("Aborting due to %s" % e)
      sys.exit(1)
    heslog.setContext({})

  ############ CF WAIT
  def CFWait(self, stackId, doneState, progressState):
    client = boto3.client('cloudformation')
    try:
      while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        response = client.describe_stacks(
          StackName=stackId
        )

        stack = response.get("Stacks", [])[0]
        status = stack.get("StackStatus")
        # use startswith because "update_complete_clenaup_in_progress"
        # is also a valid done state
        if status.startswith(doneState):
          #newline
          print
          return True
        elif status != progressState:
          self.deployFailure = True
          #newline
          print
          if status == "ROLLBACK_IN_PROGRESS":
            heslog.error(stack.get("StackStatusReason"))
          else:
            # Likely want to handle the other non-success statuses eventually
            # But this at least gives us the needed information
            print status
            print stack.get("StackStatusReason")
          return False

        time.sleep(10)
    except Exception as e:
      heslog.error(e)


  def waitCreate(self, stackId):
    if self.CFWait(stackId, "CREATE_COMPLETE", "CREATE_IN_PROGRESS"):
      heslog.info("Stack Creation Complete")


  def waitUpdate(self, stackId):
    if self.CFWait(stackId, "UPDATE_COMPLETE", "UPDATE_IN_PROGRESS"):
      heslog.info("Stack Update Complete")


  def waitDelete(self, stackId):
    if self.CFWait(stackId, "DELETE_COMPLETE", "DELETE_IN_PROGRESS"):
      heslog.info("Stack Delete Complete")


def main():
  heslog.addContext(stage="init")

  parser = argparse.ArgumentParser()
  parser.add_argument('--stage', '-s', type=str, required=True,
    help='The stage to deploy to. Must only contain alpha-numeric ascii characters')
  parser.add_argument('--config', '-c', type=str,
    help='Config file to use as input (default is config.yml)')

  # override defaults
  parser.add_argument('--deployBucket', type=str, default="testlibnd-cf",
    help='The bucket the artifacts will be put into (default is testlibnd-cf)')
  parser.add_argument('--deployFolder', type=str,
    help='Override the deployment folder (default is $SERVICE/$STAGE/$TIMESTAMP)')

  # specify functionality
  parser.add_argument('--delete', action='store_true', dest='delete',
    help="Delete the stack(s)")

  parser.add_argument('--publishOnly', action='store_true', dest='publishOnly',
    help="Publish files to the S3 bucket without calling the CF files")
  parser.add_argument('--envOnly', action='store_true', dest='envOnly',
    help="Update lambda environment without publishing/deploying")

  parser.add_argument('--noPublish', action='store_true', dest='noPublish',
    help="Don't create or publish artifacts (CF, code zip, etc) NOTE: You must override deployFolder if you specify this argument")
  parser.add_argument('--noAws', action='store_true', dest='noAws',
    help="Don't interact with aws at all")
  parser.add_argument('--keepLocal', action='store_true', dest='keepLocal',
    help="Don't delete locally created artifacts on completion")

  # Logging
  parser.add_argument('--verbose', action='store_true', dest='verbose',
    help="Verbose output")
  parser.add_argument('--debug', action='store_true', dest='debug',
    help="Debug output")

  args = parser.parse_args()

  if args.debug:
    heslog.setLevels()
  elif args.verbose:
    heslog.setLevels(heslog.LEVEL_INFO, heslog.LEVEL_WARN, heslog.LEVEL_ERROR, heslog.LEVEL_VERBOSE)
  else:
    heslog.setLevels(heslog.LEVEL_INFO, heslog.LEVEL_WARN, heslog.LEVEL_ERROR)

  timer = hesutil.Timer(True)

  confName = args.config or "config.yml"
  config = deployConfig.Config(confName, args, timestamp)

  life = Lifecycle(args, config, timer)
  life.run()

  heslog.info("Total Time: %s" % timer.end())

  if life.deployFailure:
    sys.exit(1)


if __name__ == "__main__":
  main()

