# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-alpine as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

FROM base as builder
COPY requirements.txt /requirements.txt
RUN mkdir /install
WORKDIR /install

ARG BUILD_DEPS="build-base gcc musl-dev"
RUN apk add --no-cache --virtual ${BUILD_DEPS} \
    && pip install --upgrade pip \
    && pip install --no-cache-dir --prefix=/install -r /requirements.txt \
    && apk del ${BUILD_DEPS}

FROM base
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .

CMD ["python", "app.py"]
