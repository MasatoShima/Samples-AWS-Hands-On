#!/usr/bin/env python3
"""
Name: intro_lambda_container_stack.py
Created by: Masato Shima
Created on: 2021/02/05
Description: intro_lambda_container_stack.py
"""

# **************************************************
# ----- Import Library
# **************************************************
from aws_cdk import core
from aws_cdk.core import Duration
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_lambda as lam


# **************************************************
# ----- Stack IntroLambdaContainerStack
# **************************************************
class IntroLambdaContainerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ECR Repository
        ecr_repo = ecr.Repository(
            self, "EcrRepository",
            repository_name="intro_lambda_container"
        )

        # Lambda Functions
        lam.Function(
            self, "LambdaFunctionPythonBaseImage",
            function_name="intro-lambda-container-python-base-image",
            code=lam.Code.from_ecr_image(
                repository=ecr_repo,
                tag="python-base-image"
            ),
            handler=lam.Handler.FROM_IMAGE,
            runtime=lam.Runtime.FROM_IMAGE,
            timeout=Duration.seconds(60)
        )

        lam.Function(
            self, "LambdaFunctionPythonCustomImage",
            function_name="intro-lambda-container-python-custom-image",
            code=lam.Code.from_ecr_image(
                repository=ecr_repo,
                tag="python-custom-image"
            ),
            handler=lam.Handler.FROM_IMAGE,
            runtime=lam.Runtime.FROM_IMAGE,
            timeout=Duration.seconds(60)
        )

        lam.Function(
            self, "LambdaFunctionRustCustomImage",
            function_name="intro-lambda-container-rust-custom-image",
            code=lam.Code.from_ecr_image(
                repository=ecr_repo,
                tag="rust-custom-image"
            ),
            handler=lam.Handler.FROM_IMAGE,
            runtime=lam.Runtime.FROM_IMAGE,
            timeout=Duration.seconds(60)
        )


# **************************************************
# ----- End
# **************************************************
