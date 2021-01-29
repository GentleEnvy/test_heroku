import os
import string
import random

__all__ = ['get_path_to_src', 'generate_random_token']


def get_path_to_src():
    """
    :return: absolute path to the main directory (/src)
    """
    path = os.getcwd()
    if path.endswith('\\src'):
        return path
    return path + '\\src'


_LETTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_random_token(length: int) -> str:
    """
    :return: string consisting of a random set [a-zA-Z0-9]
    """
    return ''.join(random.choice(_LETTERS) for _ in range(length))
