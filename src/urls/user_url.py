from __future__ import annotations
from typing import Any, final

from src.models import User
from src.urls.bases import UserSessionUrl

__all__ = ['UserUrl']


@final
class UserUrl(UserSessionUrl):
    """
    Before using it, you need to log in to /authorization and gets token.

    GET:
        Request:
            {
                `token`: <str>
            }
        //hr\\
        Response:
            {
                TODO: serialize user
                `id`: <int>,
                `email`: <str>,
                `password`: <str>
            }
    //hr\\
    DELETE:
        Request:
            {
                `token`: <str>
            }
        //hr\\
        Response:
            {}
    """
    @property
    def url(self) -> str:
        return '/user'

    def _get(
            self, request_json: dict[str, Any], user_session: UserUrl.Session
    ) -> dict[str, Any]:
        return user_session.user.__dict__  # TODO: serialize models to JSON

    def _delete(
            self, request_json: dict[str, Any], user_session: UserUrl.Session
    ) -> dict[str, Any]:
        user = user_session.user
        User.delete(user)
        UserUrl._delete_session(user)
        return {}
