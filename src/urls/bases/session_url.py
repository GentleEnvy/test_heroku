from __future__ import annotations
from typing import Any, Final, final
from abc import ABC, abstractmethod
from http import HTTPStatus

from flask import Request

from src.urls.exceptions import HTTPException
from src.urls.bases.base_url import BaseUrl


class SessionUrl(BaseUrl, ABC):
    """
    The IRL that supports sessions defined on each request
    """
    class Session(ABC):
        ...

    SessionKeyType = Any
    _sessions: Final[dict[SessionKeyType, Session]] = {}

    @abstractmethod
    def _get_session_key(
            self, request: Request, request_json: dict[str, Any]
    ) -> SessionKeyType:
        raise NotImplementedError

    def _parse_request(self, request: Request) -> dict[str, Any]:
        """
        :param request: current http request
        :return: parsed json with key `__session__` -> current session
        """
        request_json = super()._parse_request(request)
        session_key = self._get_session_key(request, request_json)
        try:
            session = self._sessions[session_key]
        except KeyError:
            raise HTTPException(HTTPStatus.UNAUTHORIZED, 'No session')
        request_json['__session__'] = session
        return request_json

    @staticmethod
    def __extract_session(request_json: dict[str, Any]) -> Session:
        """
        Delete entry `__session__`

        :return: current session on key `__session__` in request_json
        """
        session = request_json['__session__']
        del request_json['__session__']
        return session

    @final
    def get(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._get(request_json, self.__extract_session(request_json))

    def _get(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        """
        :param request_json: current http request in json format
        :param session: current session
        :return: GET method response
        """
        return super().get(request_json)

    @final
    def post(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._post(request_json, self.__extract_session(request_json))

    def _post(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        """
        :param request_json: current http request in json format
        :param session: current session
        :return: POST method response
        """
        return super().post(request_json)

    @final
    def put(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._put(request_json, self.__extract_session(request_json))

    def _put(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        """
        :param request_json: current http request in json format
        :param session: current session
        :return: PUT method response
        """
        return super().put(request_json)

    @final
    def delete(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._delete(request_json, self.__extract_session(request_json))

    def _delete(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        """
        :param request_json: current http request in json format
        :param session: current session
        :return: DELETE method response
        """
        return super().delete(request_json)