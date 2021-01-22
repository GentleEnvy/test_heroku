import os
import string
import random

from src import IS_HOST

__all__ = ['get_path_to_src', 'generate_random_token']


def get_path_to_src():
    """
    :return: absolute path to the main directory (/src)
    """
    if IS_HOST:
        return os.getcwd() + '/src'
    return os.getcwd()


_LETTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_random_token(length: int) -> str:
    """
    :return: string consisting of a random set [a-zA-Z0-9]
    """
    return ''.join(random.choice(_LETTERS) for _ in range(length))
