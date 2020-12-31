import os

from src import IS_HOST


def path_to_src():
    if IS_HOST:
        return os.getcwd() + '/src'
    return os.getcwd()
