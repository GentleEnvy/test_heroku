from abc import ABC
from http import HTTPStatus
from typing import Any, Final

from flask import Request

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException


class IpSessionUrl(SessionUrl, ABC):
    class Session:
        def __init__(self, ip: str):
            self.ip: Final[str] = ip

    _sessions:  dict[str, Session]

    def _get_session_key(self, request: Request, request_json: dict[str, Any]) -> Session:
        try:
            if self.app.debug:
                ip = ''
            else:
                ip = request.environ['HTTP_X_FORWARDED_FOR']  # TODO: create session
        except KeyError:
            raise HTTPException(HTTPStatus.UNAUTHORIZED, 'No IP')  # TODO: logging

        return self.Session(ip)
