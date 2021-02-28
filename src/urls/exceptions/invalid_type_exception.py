from http import HTTPStatus
from typing import Type

from src.urls.exceptions.http_exception import HTTPException

__all__ = ['InvalidTypeException']


class InvalidTypeException(HTTPException):
    def __init__(self, requirement_type: Type, name_parameter: str):
        super().__init__(
            HTTPStatus.BAD_REQUEST,
            f'`{name_parameter}` must be <{requirement_type.__name__}>'
        )
