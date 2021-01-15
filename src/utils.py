from typing import Type, TypeVar
import os

from src import IS_HOST

__all__ = ['path_to_src', 'MetaPrivateConstructor']


def path_to_src():
    if IS_HOST:
        return os.getcwd() + '/src'
    return os.getcwd()


T = TypeVar('T')


class MetaPrivateConstructor(type):
    """
    Metaclass that ensures a private constructor
    """

    def _create(cls: Type[T], *args, **kwargs) -> T:
        return super().__call__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        :raises TypeError - always
        """
        raise TypeError(
            f'{cls.__module__}.{cls.__qualname__} has no public constructor'
        )
