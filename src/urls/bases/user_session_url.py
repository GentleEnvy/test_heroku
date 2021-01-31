from __future__ import annotations

from abc import ABC
from typing import Any, Final

from src.models import User
from src.urls.bases.session_token_url import SessionTokenUrl


class UserSessionUrl(SessionTokenUrl, ABC):
    class Session(SessionTokenUrl.Session):
        def __init__(self, token: str, user: User):
            self.token: Final[str] = token
            self.user: Final[User] = user

    LENGTH_TOKEN: Final[int] = 100
    TOKEN_NAME: Final[str] = 'user_token'

    _sessions: Final[dict[str, UserSessionUrl.Session]] = {}
    __cache_user_session: Final[dict[User, UserSessionUrl.Session]] = {}

    @classmethod
    def add_user(cls, user: User) -> str:
        try:
            token = cls.__cache_user_session[user].token
        except KeyError:
            token = cls.generate_token()
            while token in cls._sessions:
                token = cls.generate_token()

        session = cls.Session(token, user)

        cls._sessions[token] = session
        cls.__cache_user_session[user] = session

        return token

    @classmethod
    def _delete_session(cls, user: User) -> None:
        try:
            session = cls.__cache_user_session[user]
            del cls._sessions[session.token]
            del cls.__cache_user_session[user]
        except KeyError:
            pass

    def _get(self, request_json, session: UserSessionUrl.Session) -> dict[str, Any]:
        return super()._get(request_json, session)

    def _post(self, request_json, session: UserSessionUrl.Session) -> dict[str, Any]:
        return super()._post(request_json, session)

    def _put(self, request_json, session: UserSessionUrl.Session) -> dict[str, Any]:
        return super()._put(request_json, session)

    def _delete(self, request_json, session: UserSessionUrl.Session) -> dict[str, Any]:
        return super()._delete(request_json, session)
