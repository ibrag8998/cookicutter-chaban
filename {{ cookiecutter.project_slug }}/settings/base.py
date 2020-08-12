from pathlib import Path

from environs import Env

# Initialize environment, read .env file
env = Env()
env.read_env()

# Base directory, which contains run.py file
BASE_DIR = Path(__file__).parent.parent

# Debug
DEBUG = env.bool("DEBUG")

# Telegram token
TELEGRAM_TOKEN = env("TELEGRAM_TOKEN")

# Packages to use by runner
PACKAGES = [
    "{{ cookiecutter.project_slug }}",
]
