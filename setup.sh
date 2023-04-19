#!/usr/bin/env bash

PYENV_HOME=$WORKSPACE/venv

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
# virtualenv $PYENV_HOME
# . $PYENV_HOME/bin/activate
# $PYENV_HOME/bin/pip install -e .
# $PYENV_HOME/bin/pytest

echo "Installing pip and requirements..."
# pip install --upgrade
sudo apt install python3-pip
pip install virtualenv
python3 -m venv $PYENV_HOME
source $PYENV_HOME/bin/activate
pip install -r requirements.txt
