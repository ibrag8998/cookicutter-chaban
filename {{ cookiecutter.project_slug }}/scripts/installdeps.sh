#!/usr/bin/env bash
cd `dirname $(realpath $0)`

. ../{{ cookiecutter.venv_path }}/bin/pip install -r ../requirements/${1:-base}.txt
