# Pulling base image
FROM python:3.8.7-alpine

# Set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --threads=4 --bind 0.0.0.0:5000 awkcalc:app
