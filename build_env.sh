#!/bin/bash
echo $0: Creating virtual environment
virtualenv-3.4 --prompt="<myenv>" ./env

mkdir ./logs
mkdir ./pids # для gunicorn

echo $0: Installing dependencies
source ./env/bin/activate
export PIP_REQUIRE_VIRTUALENV=true
./env/bin/pip3.4 install --requirement=./requirements.txt --log=./logs/build_pip_packages.log

echo $0: Making virtual environment relocatable
virtualenv-3.4 --relocatable ./env

echo $0: Creating virtual environment finished.