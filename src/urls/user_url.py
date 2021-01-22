from __future__ import annotations
from typing import Any, final

from src.models import User
from src.urls.bases import UserSessionUrl

__all__ = ['UserUrl']


@final
class UserUrl(UserSessionUrl):
    @property
    def url(self) -> str:
        return '/user'

    def _get(
            self, request_json: dict[str, Any], user_session: UserUrl.Session
    ) -> dict[str, Any]:
        return user_session.user.__dict__

    def _delete(self, request_json: dict[str, Any], user: User) -> dict[str, Any]:
        User.delete(user)
        UserUrl._delete_session(user)
        return {}
