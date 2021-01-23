"""
Util functions, classes and objects
"""
from typing import Final

from src import EMAIL_PASSWORD, DATABASE_URL
from src.utils.util_functions import get_path_to_src, generate_random_token
from src.utils.meta_private_init import MetaPrivateInit
from src.utils.email import Email
from src.utils.database import Database

__all__ = [
    'MetaPrivateInit', 'get_path_to_src', 'generate_random_token', 'email', 'database'
]

_email_login = 'komarov.sergei163@gmail.com'

email: Final[Email] = Email(_email_login, EMAIL_PASSWORD)
database: Final[Database] = Database(DATABASE_URL)
