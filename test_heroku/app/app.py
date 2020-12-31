from flask import Flask

import os


def create_app():
    app = Flask('__main__')
    print(os.getcwd())
    print(f'{os.getcwd()}/test_heroku/app/config.json')
    app.config.from_json(f'{os.getcwd()}/test_heroku/app/config.json')
    return app
