FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip -i https://mirror-pypi.runflare.com/simple

COPY requirements.txt /app/


RUN pip install --no-cache-dir -r requirements.txt -i https://mirror-pypi.runflare.com/simple

COPY . /app/