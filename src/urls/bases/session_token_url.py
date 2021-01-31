from __future__ import annotations

from abc import ABC
from http import HTTPStatus

from src.urls.bases.session_url import SessionUrl
from src.urls.exceptions import HTTPException
from src.utils.functions import generate_random_token

__all__ = ['SessionTokenUrl']


class SessionTokenUrl(SessionUrl, ABC):
    """
    The URL that supports sessions by token.
        Each request must contain entry `token` -> token of the current session
    """
    LENGTH_TOKEN: int = 10
    TOKEN_NAME: str = 'token'

    _sessions: dict[str, SessionTokenUrl.Session]

    @classmethod
    def generate_token(cls) -> str:
        """
        :return: random string token with a length == LENGTH_TOKEN
        """
        return generate_random_token(cls.LENGTH_TOKEN)

    def _get_session_key(self, request, request_json) -> str:
        """
        Delete entry TOKEN_NAME from request_json

        :return: token of the current session from request_json
        """
        token = str(self.get_value(request_json, self.TOKEN_NAME))

        del request_json[self.TOKEN_NAME]
        try:
            _ = self.__class__._sessions[token]
            return token
        except KeyError:
            raise HTTPException(
                HTTPStatus.UNAUTHORIZED,
                f'`{self.TOKEN_NAME}` is not valid'
            )
