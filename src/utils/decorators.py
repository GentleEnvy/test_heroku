from logging import exception
from typing import Callable, TypeVar

ReturnType = TypeVar('ReturnType')


def check_raises(function: Callable[..., ReturnType]) -> Callable[..., ReturnType]:
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
