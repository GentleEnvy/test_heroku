import json

from flask import Flask

from src import IS_HOST
from src.utils import path_to_src

__all__ = ['read_run_configuration', 'create_app']

_directory = f'{path_to_src()}/app/{"_production" if IS_HOST else "_development"}'


def read_run_configuration() -> dict:
    with open(f'{_directory}/run_configuration.json', 'r') as run_configuration_json:
        run_configuration = json.load(run_configuration_json)
    return run_configuration


def create_app():
    app = Flask('src.main')
    app.config.from_json(f'{_directory}/init_configuration.json')
    return app
