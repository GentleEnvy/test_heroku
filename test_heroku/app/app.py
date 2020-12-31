from flask import Flask

import os


def create_app():
    app = Flask('__main__')
    app.config.from_json('config.json')
    return app
