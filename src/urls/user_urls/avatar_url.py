from typing import Any

from src.urls.bases import UserSessionUrl


class AvatarUrl(UserSessionUrl):
    Session = UserSessionUrl.Session

    @property
    def url(self) -> str:
        return '/user/avatar'

    def _put(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        pass
