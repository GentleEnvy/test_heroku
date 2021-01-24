from __future__ import annotations

from abc import ABC
from http import HTTPStatus
from typing import Any

from flask import Request

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException
from src.utils import generate_random_token

__all__ = ['SessionTokenUrl']


class SessionTokenUrl(SessionUrl, ABC):
    """
    The URL that supports sessions by token.
        Each request must contain entry `token` -> token of the current session
    """
    LENGTH_TOKEN: int = 10

    SessionKeyType = str
    _sessions: dict[SessionKeyType, SessionTokenUrl.Session]

    @classmethod
    def generate_token(cls) -> SessionKeyType:
        """
        :return: random string token with a length == LENGTH_TOKEN
        """
        return generate_random_token(cls.LENGTH_TOKEN)

    def _get_session_key(
            self, request: Request, request_json: dict[str, Any]
    ) -> SessionKeyType:
        """
        Delete entry `token` from request_json

        :return: token of the current session from request_json
        """
        token = str(self.get_parameter(request_json, 'token'))

        del request_json['token']
        try:
            _ = self.__class__._sessions[token]
            return token
        except KeyError:
            raise HTTPException(HTTPStatus.UNAUTHORIZED, '`token` is not valid')
