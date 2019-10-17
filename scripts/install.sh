#!/bin/bash

# --- Virtual Python environment
echo "Installing project dependendencies into virtual Python environment."
PYTHON_VERSION='3.6'

PRJ_ROOT=$1

VENV_DIR=$PRJ_ROOT/venv
if [ ! -d $VENV_DIR ]; then
    virtualenv -p python$PYTHON_VERSION $VENV_DIR
fi
source $VENV_DIR/bin/activate
pip install -r $PRJ_ROOT/requirements.txt

# --- PYTHONPATH environment variable
echo "Adding PYTHONPATH to ~/.bashrc"
python $PARENT_DIR/set_pythonpath.py
