from __future__ import annotations

from abc import ABC
from http import HTTPStatus
from typing import Any, Final
from logging import warning

from src.utils.functions import generate_random_token
from src.models import User
from src.urls.bases.ip_session_url import IpSessionUrl
from src.urls.exceptions import HTTPException

__all__ = ['UserSessionUrl']


class UserSessionUrl(IpSessionUrl, ABC):
    class __UserSession:
        def __init__(self, token: str, user: User):
            self.token: Final[str] = token
            self.user: Final[User] = user

    LENGTH_TOKEN: Final[int] = 100
    NAME_TOKEN: Final[str] = 'user_token'

    __user_sessions: Final[dict[str, __UserSession]] = {}
    __cache_user_sessions: Final[dict[User, __UserSession]] = {}

    @classmethod
    def add_user_session(cls, user: User) -> str:
        if (session := cls.__cache_user_sessions.get(user)) is not None:
            return session.token

        token = cls.__generate_token()
        while token in cls.__user_sessions:
            token = cls.__generate_token()

        session = cls.__UserSession(token, user)
        cls.__user_sessions[token] = session
        cls.__cache_user_sessions[user] = session
        return token

    @classmethod
    def delete_user_session(cls, user: User) -> None:
        try:
            session = cls.__cache_user_sessions[user]
            del cls.__user_sessions[session.token]
            del cls.__cache_user_sessions[user]
        except KeyError:
            pass

    @classmethod
    def __extract_token(cls, request_json: dict[str, Any]) -> str:
        token = cls.get_value(request_json, cls.NAME_TOKEN)
        del request_json[cls.NAME_TOKEN]
        return token

    @classmethod
    def __get_session(cls, token: str) -> __UserSession:
        try:
            return cls.__user_sessions[token]
        except KeyError:
            warning(f'Not user token ({token})')
            raise HTTPException(HTTPStatus.UNAUTHORIZED, f'Not valid {cls.NAME_TOKEN}')

    @classmethod
    def __generate_token(cls):
        return generate_random_token(length=cls.LENGTH_TOKEN)

    def get(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._get(
            request_json,
            self.__get_session(self.__extract_token(request_json))
        )

    def _get(self, request_json, session: UserSessionUrl.__UserSession) -> dict[str, Any]:
        return super().get(request_json)

    def post(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._post(
            request_json,
            self.__get_session(self.__extract_token(request_json))
        )

    def _post(
            self,
            request_json,
            session: UserSessionUrl.__UserSession
    ) -> dict[str, Any]:
        return super().post(request_json)

    def put(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._put(
            request_json,
            self.__get_session(self.__extract_token(request_json))
        )

    def _put(self, request_json, session: UserSessionUrl.__UserSession) -> dict[str, Any]:
        return super().put(request_json)

    def delete(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return self._delete(
            request_json,
            self.__get_session(self.__extract_token(request_json))
        )

    def _delete(
            self,
            request_json,
            session: UserSessionUrl.__UserSession
    ) -> dict[str, Any]:
        return super().delete(request_json)
