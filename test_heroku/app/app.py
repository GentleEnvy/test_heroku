from flask import Flask

import os


def create_app():
    app = Flask('__main__')
    print(os.getcwd())
    print(f'{os.getcwd()}/app/config.json')
    app.config.from_json(f'{os.getcwd()}/app/config.json')
    return app
