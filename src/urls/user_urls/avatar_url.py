from typing import Any
import base64
import binascii
from http import HTTPStatus

from src.urls.bases import UserSessionUrl
from src.urls.exceptions import HTTPException
from src.utils import image_base

__all__ = ['AvatarUrl']


class AvatarUrl(UserSessionUrl):
    r"""
    PUT:
        Request:
            {
                `user_token`: <str> - the token received during authorization,
                `avatar_data`: <str> - bytes of the avatar encoded in
            }
        Response:
            {
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
    Session = UserSessionUrl.Session

    @property
    def url(self) -> str:
        return '/user/avatar'

    def _put(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        try:
            avatar_data: bytes = base64.b64decode(
                self.get_value(request_json, 'avatar_data')
            )
        except binascii.Error:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                '`avatar_data` encoding must be base64 (/+)'
            )
        try:
            avatar_url = image_base.save(avatar_data)
        except ValueError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                'invalid `avatar_data`'
            )
        ################################## FIXME
        with open('image.jpg', 'wb') as f:
            f.write(avatar_data)
        ################################## FIXME
        user = session.user
        if old_avatar_url := user.avatar_url:
            image_base.delete(old_avatar_url)

        user.avatar_url = avatar_url
        return {
            'avatar_url': avatar_url
        }

    def _delete(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        user = session.user
        if avatar_url := user.avatar_url:
            image_base.delete(avatar_url)
        del user.avatar_url
        return {}
