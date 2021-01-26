from __future__ import annotations

from typing import Any, final

from src.models import User
from src.urls.bases import UserSessionUrl

__all__ = ['UserUrl']


@final
class UserUrl(UserSessionUrl):
    r"""
    Before using it, you need to log in to /authorization and gets token.
    //hr\\
    GET:
        Request:
            {
                `token`: <str> - the token received during authorization
            }
        Response:
            {
                `id`: <int>,
                `email`: <str>,
                `password`: <str>
            }
    //hr\\
    DELETE:
        Request:
            {
                `token`: <str> - the token received during authorization
            }
        Response:
            {}
    """
    Session = UserSessionUrl.Session

    @property
    def url(self) -> str:
        return '/user'

    def _get(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        return session.user.serialize()

    def _delete(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        user = session.user
        User.delete(user)
        UserUrl._delete_session(user)
        return {}
