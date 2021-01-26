from flask import Flask

from src.urls.index import Index
from src.urls.log_io import Authorization, EmailUrl, Registration
from src.urls.user_urls.user_url import UserUrl

__all__ = ['init_urls']


def init_urls(app: Flask):
    Registration(app)
    Authorization(app)
    UserUrl(app)
    EmailUrl(app)
    Index(app)
