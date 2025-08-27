#!/usr/bin/env python3
from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from cdk_fun.cdk_fun_stack import CdkFunStack

existing_environment = core.Environment(
    # can use env imports if using Dev / UAT / Prod
    account = "533267147140", # Your AWS Account
    region = "eu-west-1" # Your AWS Region
)

app = core.App()
CdkFunStack(
    app,
    "CdkFunStack",
    env = existing_environment
)

app.synth()