from typing import Any, Final, final

from src.models import User
from src.urls.bases import IpSessionUrl, UserSessionUrl

__all__ = ['Authorization']


@final
class Authorization(IpSessionUrl):
    r"""
    GET:
        Request:
            {
                `email`: <str>,
                `password`: <str>
            }
        Response:
            {
                `user_token`: <str> - session token for user identification, used for any requests from this user
            }
            or
            {
                `error`: <int>(
                    1 - if no user with this email address
                    or
                    2 - if the password is incorrect
                )
            }
    """
    url: Final[str] = '/authorization'

    def _get(self, request_json, session) -> dict[str, Any]:
        email = str(self.get_value(request_json, 'email'))
        password = str(self.get_value(request_json, 'password'))

        user = User.get(email)
        if user is None:
            return {'error': 1}
        if user.password != password:
            return {'error': 2}

        user_token = UserSessionUrl.add_user(user)
        return {
            'user_token': user_token
        }
