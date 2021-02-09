# """
# Name: Dockerfile
# Created by: Masato Shima
# Created on: 2021/02/07
# Description: Dockerfile
# """

# Build image
FROM public.ecr.aws/lambda/provided:al2 AS build-stage

WORKDIR /opt/

ENV PATH $PATH:/root/.cargo/bin

RUN yum install -y gcc && \
    curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain stable && \
    rustup install stable

ADD src ./src/
COPY ./* ./

RUN cargo build --release

# Runtime image
FROM public.ecr.aws/lambda/provided:al2

COPY --from=build-stage /opt/target/release/rust_custom_image ${LAMBDA_RUNTIME_DIR}/bootstrap

CMD [ "lambda-handler" ]

# End
