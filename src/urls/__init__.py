from flask import Flask

from src.urls._index import Index
from src.urls._echo import Echo
# noinspection PyProtectedMember
from src.urls._log_io import Authorization, EmailUrl, Registration
# noinspection PyProtectedMember
from src.urls._user_urls import UserUrl, AvatarUrl

__all__ = ['init_urls']


def init_urls(app: Flask):
    Registration(app)
    Authorization(app)
    UserUrl(app)
    AvatarUrl(app)
    EmailUrl(app)
    Index(app)
    Echo(app)
