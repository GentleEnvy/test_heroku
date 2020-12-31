from flask import Flask

import os


def create_app():
    print(f'cd app: {os.getcwd()}')
    return Flask('__main__')
