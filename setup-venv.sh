#!/usr/bin/env bash

PATH=$WORKSPACE/venv
if [ -d "venv" ]; then
    rm -rf $PATH
fi

echo "Installing pip and creating venv..."
# pip install --upgrade
# pip install virtualenv
# sudo python3 -m venv $PATH

echo "Activating virtual environment ..."
# . venv/bin/activate

echo "Installing requirements..."
# pip install -r requirements.txt --download-cache=/tmp/$JOB_NAME
