from pathlib import Path

from environs import Env

# Initialize environment, read .env file
env = Env()
env.read_env()

# Base directory, which contains run.py file
BASE_DIR = Path(__file__).parent.parent

# Debug
DEBUG = env.bool("DEBUG")
if DEBUG is None:
    raise EnvironmentError("DEBUG env variable is required, but not set")

# Telegram token
TELEGRAM_TOKEN = env("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise EnvironmentError("TELEGRAM_TOKEN env variable is required, but not set")

# Packages to use by runner
PACKAGES = [
    "{{ cookiecutter.project_slug }}",
]
