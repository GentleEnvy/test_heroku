from flask import Flask

from src import ON_HOSTING
from src.utils import get_path_to_src

__all__ = ['create_app']


def create_app():
    """
    :return: flask app with config from dev_config.json
    """
    app = Flask('src.main')
    if ON_HOSTING:
        app.config.from_json(f'{get_path_to_src()}/app/prod_config.json')
    else:
        app.config.from_json(f'{get_path_to_src()}/app/dev_config.json')
    return app
