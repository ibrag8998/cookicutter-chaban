#!/usr/bin/env python3
import os

from chaban.core.runner import runner

if __name__ == "__main__":
    os.environ.setdefault("CHABAN_SETTINGS_MODULE", "settings")
    runner.run(__file__)
