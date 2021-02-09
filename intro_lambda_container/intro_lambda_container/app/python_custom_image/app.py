#!/usr/bin/env python3
"""
Name: app.py
Created by: Masato Shima
Created on: 2021/02/06
Description: Sample lambda application.
"""

# **************************************************
# ----- Import Library
# **************************************************
from typing import Any, Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext


# **************************************************
# ----- Set logger
# **************************************************
logger = Logger()


# **************************************************
# ----- Lambda handler
# **************************************************
@logger.inject_lambda_context()
def lambda_handler(event: Dict[str, Any], context: LambdaContext) -> Dict[str, Any]:
    logger.info({"event": event})
    logger.info({"context": context})

    response = {
        "message": "Hello Lambda Container ! (Python Custom Image)"
    }

    return response


# **************************************************
# ----- End
# **************************************************
