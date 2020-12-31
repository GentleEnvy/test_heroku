from flask import Flask

from .base_url import BaseUrl

from .index import Index

__all__ = ['init_urls']


def init_urls(app: Flask):
    print(BaseUrl.classes)
    for url_class in BaseUrl.classes:
        url_class(app)
