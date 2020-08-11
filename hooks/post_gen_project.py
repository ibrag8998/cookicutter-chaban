import os

# get cwd
cwd = os.getcwd()

# rename "gitignore" to ".gitignore"
gitignore_file = os.path.join(cwd, "gitignore")
os.rename(gitignore_file, "." + gitignore_file)
