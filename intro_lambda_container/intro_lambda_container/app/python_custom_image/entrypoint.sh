#!/bin/sh
# """
# Name: entrypoint.sh
# Created by: Masato Shima
# Created on: 2021/02/07
# Description: entrypoint.sh
# """

if [ -n "${AWS_LAMBDA_RUNTIME_API}" ]; then
    exec /usr/local/bin/python -m awslambdaric "$1"
else
    exec /usr/bin/aws-lambda-rie /usr/local/bin/python -m awslambdaric "$1"
fi

# End
