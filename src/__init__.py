# noinspection SpellCheckingInspection
"""
Environment requirements:
    IS_HOST: Literal[0, 1] - 1, if the program runs on the hosting, else 0
    DATABASE_URL: <str>
    EMAIL_LOGIN: <str> - login of the main email account
    EMAIL_PASSWORD: <str> - password of the main email account
    CLOUDNARY_NAME: <str> - cloudnary app name
    CLOUDNARY_KEY: <int> - cloudnary app key
    CLOUDNARY_SECRET: <str> - cloudnary app secret
"""
import os
from typing import Final

# noinspection SpellCheckingInspection
__all__ = [
    'IS_HOST', 'DATABASE_URL', 'EMAIL_LOGIN', 'EMAIL_PASSWORD',
    'CLOUDNARY_NAME', 'CLOUDNARY_KEY', 'CLOUDNARY_SECRET'
]

print(__name__)

IS_HOST: Final[bool] = bool(int(os.environ['IS_HOST']))
DATABASE_URL: Final[str] = os.environ['DATABASE_URL']
EMAIL_LOGIN: Final[str] = os.environ['EMAIL_LOGIN']
EMAIL_PASSWORD: Final[str] = os.environ['EMAIL_PASSWORD']
# noinspection SpellCheckingInspection
CLOUDNARY_NAME: Final[str] = os.environ['CLOUDNARY_NAME']
# noinspection SpellCheckingInspection
CLOUDNARY_KEY: Final[int] = int(os.environ['CLOUDNARY_KEY'])
# noinspection SpellCheckingInspection
CLOUDNARY_SECRET: Final[str] = os.environ['CLOUDNARY_SECRET']
