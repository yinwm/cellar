#!/bin/sh

export PYTHONPATH=$PYTHONPATH:./lib

. venv/bin/activate

python $*
