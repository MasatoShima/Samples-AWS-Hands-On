# """
# Name: Dockerfile
# Created by: Masato Shima
# Created on: 2021/02/05
# Description: Dockerfile
# """

FROM public.ecr.aws/lambda/python:3.8

WORKDIR /var/task/

COPY app.py ./
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["app.lambda_handler"]

# End
