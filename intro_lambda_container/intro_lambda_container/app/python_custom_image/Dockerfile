# """
# Name: Dockerfile
# Created by: Masato Shima
# Created on: 2021/02/06
# Description: Dockerfile
# """

ARG FUNCTION_DIR="/home/app/"
ARG RUNTIME_VERSION="3.9"
ARG DISTRO_VERSION="3.13"

# Bundle build image + runtime image
FROM python:${RUNTIME_VERSION}-alpine${DISTRO_VERSION} AS python-alpine
RUN apk add --no-cache \
    libstdc++

# Build stage
FROM python-alpine AS build-stage

ARG FUNCTION_DIR
ARG RUNTIME_VERSION

RUN apk add --no-cache \
    build-base \
    libtool \
    autoconf \
    automake \
    libexecinfo-dev \
    make \
    cmake \
    libcurl

RUN mkdir -p ${FUNCTION_DIR}

COPY app.py ${FUNCTION_DIR}
COPY requirements.txt ${FUNCTION_DIR}

RUN python${RUNTIME_VERSION} -m pip install -r ${FUNCTION_DIR}requirements.txt -t ${FUNCTION_DIR}

# Runtime image
FROM python-alpine

ARG FUNCTION_DIR
ARG RUNTIME_VERSION

WORKDIR ${FUNCTION_DIR}

COPY --from=build-stage ${FUNCTION_DIR} ${FUNCTION_DIR}
COPY entrypoint.sh /
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie

RUN chmod 775 /entrypoint.sh && \
    chmod 755 /usr/bin/aws-lambda-rie

ENTRYPOINT ["/entrypoint.sh"]

CMD ["app.lambda_handler"]

# End
