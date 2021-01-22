"""
Environment requirements:
    IS_HOST: Literal[0, 1] - 1, if the program runs on the hosting, else 0
    DATABASE_URL: <str>
    EMAIL_PASSWORD: <str> - password of the email from which the confirmation email comes
"""

import os

__all__ = ['IS_HOST', 'DATABASE_URL', 'EMAIL_PASSWORD']

IS_HOST: bool = bool(int(os.environ['IS_HOST']))
DATABASE_URL: str = os.environ['DATABASE_URL']
EMAIL_PASSWORD: str = os.environ['EMAIL_PASSWORD']
