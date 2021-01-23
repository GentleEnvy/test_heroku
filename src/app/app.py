from flask import Flask

from src import IS_HOST
from src.utils import get_path_to_src

__all__ = ['create_app']

_directory = f'{get_path_to_src()}/app/{"production" if IS_HOST else "development"}'


def create_app():
    """
    :return: flask app with config from configuration.json
    """
    app = Flask('src.main')
    app.config.from_json(f'{_directory}/configuration.json')
    return app
