from logging import exception
from typing import Callable, TypeVar

__all__ = ['check_raises']

_ReturnType = TypeVar('_ReturnType')


def check_raises(function: Callable[..., _ReturnType]) -> Callable[..., _ReturnType]:
    def check(*args, **kwargs):
        # noinspection PyBroadException
        try:
            return function(*args, **kwargs)
        except Exception:
            # noinspection PyUnresolvedReferences
            exception(
                f'''(
    {function.__module__ = },
    {function.__name__ = }
): {{
    {args = },
    {kwargs = }
}}'''
            )
            raise

    return check
