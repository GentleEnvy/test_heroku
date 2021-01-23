from typing import Any, Final, final
from abc import ABC, abstractmethod
from http import HTTPStatus

from flask import Flask
from flask import Request

from src.utils import generate_random_token
from src.urls.bases.session_token_url import SessionTokenUrl
from src.urls.exceptions import HTTPException, NoParameterException
from src.models import User


class UserSessionUrl(SessionTokenUrl, ABC):
    class Session(SessionTokenUrl.Session):
        def __init__(self, token: str, user: User):
            self.token: Final[str] = token
            self.user: Final[User] = user

    LENGTH_TOKEN: Final[int] = 100

    SessionKeyType = SessionTokenUrl.SessionKeyType
    _sessions: dict[SessionKeyType, Session]

    __cache_user_session: Final[dict[User, Session]] = {}

    @classmethod
    def add_user(cls, user: User) -> SessionKeyType:
        try:
            token = cls.__cache_user_session[user].token
        except KeyError:
            token = cls.generate_token()
            while token in cls._sessions:
                token = cls.generate_token()

        session = cls.Session(token, user)

        cls._sessions[token] = session
        cls.__cache_user_session[user] = session

        print(f'{cls._sessions = }')
        print(f'{cls.__cache_user_session = }')
        print(f'{session = }')

        return token

    @classmethod
    def _delete_session(cls, user: User) -> None:
        try:
            session = cls.__cache_user_session[user]
            del cls._sessions[session.token]
            del cls.__cache_user_session[user]
        except KeyError:
            pass
