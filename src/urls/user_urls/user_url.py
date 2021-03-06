from __future__ import annotations

from typing import Any, Final, final

from src.models import User
from src.urls.bases import UserSessionUrl
from src.utils import image_base

__all__ = ['UserUrl']


@final
class UserUrl(UserSessionUrl):
    r"""
    Before using it, you need to log in to /authorization and gets token.
    //hr\\
    GET:
        Request:
            {
                `user_token`: <str> - the token received during authorization
            }
        Response:
            {
                `id`: <int>,
                `email`: <str>,
                `password`: <str>,
                `avatar_url`: <str>
            }
    //hr\\
    DELETE:
        Request:
            {
                `user_token`: <str> - the token received during authorization
            }
        Response:
            {}
    """
    url: Final[str] = '/user'

    def _get(self, request_json, session) -> dict[str, Any]:
        return session.user.serialize()

    def _delete(self, request_json, session) -> dict[str, Any]:
        user = session.user
        if avatar_url := user.avatar_url:
            image_base.delete(avatar_url)
        User.delete(user)
        UserUrl._delete_session(user)
        return {}
