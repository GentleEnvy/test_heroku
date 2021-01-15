from typing import Union
from http import HTTPStatus

__all__ = ['HTTPException']


_HTTP_CODE_STATUS: dict[int, HTTPStatus] = {
    http_status.value: http_status for http_status in HTTPStatus
}


class HTTPException(Exception):
    def __init__(
            self,
            http_status: Union[int, HTTPStatus] = HTTPStatus.INTERNAL_SERVER_ERROR,
            message: str = ''
    ):
        """
        :raises ValueError: if `http_status` is OK(200)
        """
        self._http_status: HTTPStatus
        if type(http_status) == int:
            self._http_status = _HTTP_CODE_STATUS[http_status]
        else:
            self._http_status = http_status
        if self._http_status == HTTPStatus.OK:
            raise ValueError('`http_status` must not be OK')
        self._message: str = message

    @property
    def http_status(self) -> HTTPStatus:
        return self._http_status

    @property
    def message(self) -> str:
        return self._message

    def __str__(self) -> str:
        return f'{self._http_status.phrase}({self._http_status.value}): ' \
               f'{self._message if self._message else self._http_status.description}'
