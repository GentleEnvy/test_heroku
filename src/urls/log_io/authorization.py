from typing import Any, final

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
                `token`: <str> - session token for user identification, used for any requests from this user
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
    Session = IpSessionUrl.Session

    @property
    def url(self) -> str:
        return '/authorization'

    def _get(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        email = str(self.get_parameter(request_json, 'email'))
        password = str(self.get_parameter(request_json, 'password'))

        user = User.get(email)
        if user is None:
            return {'error': 1}
        if user.password != password:
            return {'error': 2}

        token = UserSessionUrl.add_user(user)
        return {
            'token': token
        }
