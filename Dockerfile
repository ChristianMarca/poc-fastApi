FROM ubuntu:18.04

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get install -y python3.7 python3-pip \
    && apt-get install -y python3-distutils python3-setuptools

RUN python3.7 -m pip install pip && python3.7 -m pip install pipenv

RUN apt-get install -y htop

RUN mkdir -p /usr/src/poc-fastApi

WORKDIR /usr/src/poc-fastApi

COPY . .

ENV PIPENV_VENV_IN_PROJECT="enabled"

RUN pipenv install --deploy --ignore-pipfile --python '/usr/bin/python3.7'

ENV PYTHONPATH="/usr/src/poc-fastApi:$PYTHONPATH"

EXPOSE 8000

CMD pipenv run uvicorn main:app --host 0.0.0.0 --port 8000
