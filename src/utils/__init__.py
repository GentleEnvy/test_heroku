"""
Util functions, classes and objects
"""
from typing import Final

from src import (
    DATABASE_URL, EMAIL_LOGIN, EMAIL_PASSWORD,
    CLOUDNARY_NAME, CLOUDNARY_KEY, CLOUDNARY_SECRET
)
from src.utils.interfaces import Database, Email, ImageBase
from src.utils.util_functions import get_path_to_src, generate_random_token
from src.utils.meta_private_init import MetaPrivateInit
from src.utils._smtp_email import SmtpEmail
from src.utils._postgresql import PostgreSql
from src.utils._cloudnary import Cloudnary

__all__ = [
    'MetaPrivateInit', 'get_path_to_src', 'generate_random_token', 'email', 'database',
    'image_base'
]

email: Final[Email] = SmtpEmail(EMAIL_LOGIN, EMAIL_PASSWORD)
database: Final[Database] = PostgreSql(DATABASE_URL)
image_base: Final[ImageBase] = Cloudnary(
    cloud_name=CLOUDNARY_NAME,
    api_key=CLOUDNARY_KEY,
    api_secret=CLOUDNARY_SECRET
)
