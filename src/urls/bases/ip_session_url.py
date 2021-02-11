from __future__ import annotations

from abc import ABC
from http import HTTPStatus
from logging import warning
from typing import Any, Optional, Final, final
from datetime import datetime, timedelta

from flask import Flask, Response, Request

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException

__all__ = ['IpSessionUrl']


def _get_ip(request: Request) -> Optional[str]:
    env = request.environ
    return env.get('HTTP_X_FORWARDED_FOR') or env.get('REMOTE_ADDR')


class IpSessionUrl(SessionUrl, ABC):
    """
    The URL that supports sessions by IP. To get an IP, a proxy is required
    """
    class Session(SessionUrl.Session):
        def __init__(self, ip: str):
            self.ip: Final[str] = ip
            self.__time_requests: set[datetime] = set()

        @property
        def ban_count(self) -> int:
            return 10

        @property
        def ban_seconds(self) -> float:
            return 60

        def mark(self, request: Request):
            now = datetime.now()
            delta = timedelta(0, self.ban_seconds)
            for time_request in self.__time_requests:
                if (now - time_request) > delta:
                    self.__time_requests.remove(time_request)


    class __GlobalSession(Session):
        pass

    _sessions: dict[str, IpSessionUrl.Session] = {}
    __sessions: Final[dict[str, __GlobalSession]] = {}

    @classmethod
    def __add_session(cls, ip: str) -> Session:
        session = cls.Session(ip)
        cls._sessions[ip] = session
        return session

    @classmethod
    def __check_session(cls, session: Session) -> bool:
        pass

    def _get_request(self) -> Request:
        request = super()._get_request()
        if ip := _get_ip(request) is None:
            warning(f'No IP in request (\n\t{request.environ = }\n)')
            raise HTTPException(HTTPStatus.UNAUTHORIZED, 'No IP')

        if global_session := IpSessionUrl.__sessions.get(ip) is None:
            global_session = IpSessionUrl.__GlobalSession(ip)
            IpSessionUrl.__sessions[ip] = global_session



        if local_session := self._sessions.get(ip) is None:
            local_session = self.__add_session(ip)

        return request

    @final
    def _get_session_key(self, request, request_json) -> str:
        return _get_ip(request)

    def _get(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._get(request_json, session)

    def _post(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._post(request_json, session)

    def _put(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._put(request_json, session)

    def _delete(self, request_json, session: IpSessionUrl.Session) -> dict[str, Any]:
        return super()._delete(request_json, session)
