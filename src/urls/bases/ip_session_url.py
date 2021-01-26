from abc import ABC
from http import HTTPStatus
from typing import Any, Final

from flask import Request

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException


class IpSessionUrl(SessionUrl, ABC):
    """
    The URL that supports sessions by IP. To get an IP, a proxy is required
    """
    class Session:
        def __init__(self, ip: str):
            self.ip: Final[str] = ip

    _sessions:  Final[dict[str, Session]] = {}

    @classmethod
    def __add_session(cls, ip: str) -> None:
        cls._sessions[ip] = cls.Session(ip)

    def _get_session_key(self, request: Request, request_json: dict[str, Any]) -> str:
        """
        :return: IP from HTTP_X_FORWARDED_FOR
        :raises HTTPException: if no HTTP_X_FORWARDED_FOR in request
        """
        try:
            if self.app.debug:
                ip = ''
            else:
                ip = request.environ['HTTP_X_FORWARDED_FOR']  # TODO: create session
        except KeyError:
            raise HTTPException(HTTPStatus.UNAUTHORIZED, 'No IP')  # TODO: logging

        if ip not in IpSessionUrl._sessions:
            IpSessionUrl.__add_session(ip)

        return ip
