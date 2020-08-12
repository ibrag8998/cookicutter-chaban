#!/usr/bin/env bash
cd `dirname $(realpath $0)`

req_type = ${1:-base}

. ../{{ cookiecutter.venv_path }}/bin/pip install -r ../requirements/$1.txt
