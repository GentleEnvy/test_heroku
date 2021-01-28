from __future__ import annotations

from abc import ABC
from http import HTTPStatus
from typing import Any, Final

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException


class IpSessionUrl(SessionUrl, ABC):
    """
    The URL that supports sessions by IP. To get an IP, a proxy is required
    """
    class Session(SessionUrl.Session):
        def __init__(self, ip: str):
            self.ip: Final[str] = ip

    _sessions: Final[dict[str, IpSessionUrl.Session]] = {}

    @classmethod
    def __add_session(cls, ip: str) -> None:
        cls._sessions[ip] = cls.Session(ip)

    def _get_session_key(self, request, request_json) -> str:
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

    def _get(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._get(request_json, session)

    def _post(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._post(request_json, session)

    def _put(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._put(request_json, session)

    def _delete(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._delete(request_json, session)
