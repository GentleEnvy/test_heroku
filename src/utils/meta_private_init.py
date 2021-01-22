from typing import TypeVar, Type

__all__ = ['MetaPrivateInit']

T = TypeVar('T')


class MetaPrivateInit(type):
    """
    Metaclass that ensures a private __init__
    """
    def _create(cls: Type[T], *args, **kwargs) -> T:
        """
        :param args, kwargs: parameters specified in current __init__
        :return: object created from the current __init__
        """
        return super().__call__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        """
        :raises TypeError - always
        """
        raise TypeError(
            f'{cls.__module__}.{cls.__qualname__} has no public __init__'
        )
