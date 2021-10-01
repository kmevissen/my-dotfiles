FROM travix/base-alpine:3.4

MAINTAINER Travix

RUN apk --update add python=2.7.14-r0 py-setuptools=20.8.0-r0

COPY src /src
WORKDIR /src

ENTRYPOINT ["python", "main.py"]