"""
Environment requirements:
    IS_HOST: Literal[0, 1] - 1, if the program runs on the hosting, else 0
"""

import os

try:
    IS_HOST = bool(int(os.environ['IS_HOST']))
except (KeyError, ValueError):
    IS_HOST = False
