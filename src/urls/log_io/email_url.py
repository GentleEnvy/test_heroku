from __future__ import annotations
from typing import Any, Final
from http import HTTPStatus

from flask import Request

from src.utils import generate_random_token
from src.models import User
from src.urls.exceptions import HTTPException
from src.urls.bases import SessionTokenUrl, UserSessionUrl

__all__ = ['EmailUrl']


class EmailUrl(SessionTokenUrl):
    class Session(SessionTokenUrl.Session):
        def __init__(self, token: str, email: str, password: str, code: int):
            self.token: Final[str] = token
            self.email: Final[str] = email
            self.password: Final[str] = password
            self.code: Final[int] = code

    LENGTH_TOKEN: Final[int] = 30

    SessionKeyType = SessionTokenUrl.SessionKeyType
    _sessions: dict[SessionKeyType, Session]

    __cache_email_session: Final[dict[str, Session]] = {}
    __cache_code_session: Final[dict[int, Session]] = {}

    @classmethod
    def add_email(cls, email: str, password: str, code: int) -> str:
        try:
            token = cls.__cache_email_session[email].token
        except KeyError:
            token = cls.generate_token()
            while token in cls._sessions:
                token = cls.generate_token()

        session = cls.Session(token, email, password, code)

        try:
            session_with_same_code = cls.__cache_code_session[code]
            cls._delete_session(session_with_same_code.email)
        except KeyError:
            pass

        cls._sessions[token] = session
        cls.__cache_email_session[email] = session
        cls.__cache_code_session[code] = session

        return token

    @classmethod
    def _delete_session(cls, email: str) -> None:
        try:
            session = cls.__cache_email_session[email]
            del cls._sessions[session.token]
            del cls.__cache_email_session[email]
            del cls.__cache_code_session[session.code]
        except KeyError:
            pass

    @property
    def url(self) -> str:
        return '/email'

    def _post(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        code = self.get_parameter(request_json, 'code')
        if code == session.code:
            # TODO: handle same email in database
            user = User.register(session.email, session.password)
            EmailUrl._delete_session(session.email)
            token = UserSessionUrl.add_user(user)
            return {
                'token': token
            }
        return {
            'error': 1
        }