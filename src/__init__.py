"""
Environment requirements:
    IS_HOST: Literal[0, 1] - 1, if the program runs on the hosting, else 0
    DATABASE_URL: str
"""

import os

__all__ = ['IS_HOST', 'DATABASE_URL']

IS_HOST: bool = bool(int(os.environ['IS_HOST']))
DATABASE_URL: str = os.environ['DATABASE_URL']
