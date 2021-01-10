from flask import Flask

from src import IS_HOST
from src.utils import path_to_src

__all__ = ['create_app']

_directory = f'{path_to_src()}/app/{"_production" if IS_HOST else "_development"}'


def create_app():
    app = Flask('src.main')
    app.config.from_json(f'{_directory}/configuration.json')
    return app
