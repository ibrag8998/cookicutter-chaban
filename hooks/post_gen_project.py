import os

print(os.getcwd())
print(os.path.abspath('{{ cookiecutter.project_slug }}'))
