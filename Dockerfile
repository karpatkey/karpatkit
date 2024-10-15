FROM python:3.10-slim
ARG DEBIAN_FRONTEND=noninteractive

###############################################################################
# Base

RUN apt-get update \
 && apt-get install -y --no-install-recommends eatmydata 
###############################################################################
# DEPS

RUN eatmydata apt-get update \
 && eatmydata apt-get install -y --no-install-recommends vim git

RUN pip install --upgrade pip \
 && pip install --no-cache-dir ipython
###############################################################################
# CODE

WORKDIR /repo

COPY . /repo
RUN pip install --no-cache-dir .
RUN pip install --no-cache-dir -r requirements-dev.txt

ENV PYTHONPATH /repo

RUN useradd kkit

