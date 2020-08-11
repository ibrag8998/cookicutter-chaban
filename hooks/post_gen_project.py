import os

print(" ~~ Creating virtual environment ...")
os.system("python3 -m venv {{ cookiecutter.venv_path }}")
print(" == Done")

print(" ~~ Installing local python requirements ...")
os.system("./venv/bin/pip install -r requirements/local.txt > /dev/null")
print(" == Done")
