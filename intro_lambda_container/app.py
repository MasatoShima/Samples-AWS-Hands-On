#!/usr/bin/env python3
"""
Name: app.py
Created by: Masato Shima
Created on: 2021/02/05
Description: app.py
"""

# **************************************************
# ----- Import Library
# **************************************************
from aws_cdk import core

from intro_lambda_container.intro_lambda_container_stack import IntroLambdaContainerStack


# **************************************************
# ----- Applications
# **************************************************
app = core.App()

IntroLambdaContainerStack(app, "intro-lambda-container")

app.synth()


# **************************************************
# ----- End
# **************************************************
