import os
import random
import string
from typing import TextIO

__all__ = ['get_path_to_src', 'generate_random_token', 'file_line_count']


def get_path_to_src():
    """
    :return: absolute path to the main directory (/src)
    """
    path = os.getcwd()
    if path.endswith('/src') or path.endswith('\\src'):
        return path
    return path + '/src'


_LETTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits


def generate_random_token(length: int) -> str:
    """
    :return: string consisting of a random set [a-zA-Z0-9]
    """
    return ''.join(random.choice(_LETTERS) for _ in range(length))


def file_line_count(file: TextIO) -> int:
    """
    :param file: file is opened in 'r' mode
    :return: number of lines in file
    """
    line_count = 0
    for last_line, _ in enumerate(file):
        line_count = last_line
    return line_count
