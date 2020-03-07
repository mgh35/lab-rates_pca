#!/bin/bash
set -e

./make-env.sh
source .venv/bin/activate
pip install -r requirements-lock.txt

python setup.py develop

jupyter lab ./notebooks
