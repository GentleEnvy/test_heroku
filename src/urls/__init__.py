from flask import Flask

from src.urls.log_io import Registration, Authorization, EmailUrl
from src.urls.user_url import UserUrl
from src.urls.index import Index

__all__ = ['init_urls']


def init_urls(app: Flask):
    Registration(app)
    Authorization(app)
    UserUrl(app)
    EmailUrl(app)
    Index(app)
