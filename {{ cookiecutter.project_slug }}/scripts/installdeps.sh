#!/usr/bin/env bash
cd `dirname $(realpath $0)`

. ../venv/bin/activate

pip install -r ../requirements/${1:-base}.txt

