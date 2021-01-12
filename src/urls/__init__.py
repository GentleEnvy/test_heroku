from flask import Flask

from src.urls.base_url import BaseUrl

from src.urls.index import Index

__all__ = ['init_urls']


def init_urls(app: Flask):
    for url_class in BaseUrl.classes:
        url_class(app)
