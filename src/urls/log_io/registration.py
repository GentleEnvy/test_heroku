from typing import Optional, Any, Final, final
from http import HTTPStatus
import re

from flask import Flask
from flask import Request

from src.utils import email as util_email
from src.urls.exceptions import HTTPException, NoParameterException
from src.urls.bases import IpSessionUrl, UserSessionUrl
from src.urls.log_io.email_url import EmailUrl
from src.models import User

__all__ = ['Registration']

_MAIL_REGEX: Final[re.Pattern] = re.compile(
    '^[a-zA-Z0-9]+([-._][a-zA-Z0-9]+)*@'
    '[a-zA-Z0-9]+([-.][a-zA-Z0-9]+)*\\.[a-zA-Z]{2,7}$'
)
_PASSWORD_REGEX: Final[re.Pattern] = re.compile('^[a-zA-z0-9_]{6,}$')
_DEFAULT_MESSAGE: Final[str] = 'code: %s'  # TODO: read message from file


def _check_email_valid(email: str) -> bool:
    return bool(re.fullmatch(_MAIL_REGEX, email))


def _check_password_valid(password: str) -> bool:
    return bool(re.fullmatch(_PASSWORD_REGEX, password))


def _check_unique_email(email: str) -> bool:
    return User.get(email) is None


def _send_code(email: str, code: int) -> None:
    util_email.send(
        message=_DEFAULT_MESSAGE % code,
        to=email
    )


@final
class Registration(IpSessionUrl):
    r"""
    POST:
        Request:
            {
                `email`: <str>,
                `password`: <str>
            }
        Response:
            {
                `token`: <str> - used to identify the registrant for check the email code
            }
            or
            {
                `error`: <int>(
                    1 - if a user with this email already exists
                    or
                    2 - if could not send email
                )
            }
    """
    Session = IpSessionUrl.Session

    def __init__(self, app: Flask):
        super().__init__(app)
        self.__last_code = 999  # start code == 1000

    @property
    def _code(self) -> int:
        if self.__last_code == 9999:
            self.__last_code = 999
        self.__last_code += 1
        return self.__last_code

    @property
    def url(self) -> str:
        return '/registration'

    def _post(self, request_json: dict[str, Any], session: Session) -> dict[str, Any]:
        email = str(self.get_parameter(request_json, 'email'))
        password = str(self.get_parameter(request_json, 'password'))

        if not _check_email_valid(email):
            raise HTTPException(HTTPStatus.BAD_REQUEST, '`email` is not valid')
        if not _check_password_valid(password):
            raise HTTPException(HTTPStatus.BAD_REQUEST, '`password` is not valid')

        if not _check_unique_email(email):
            return {'error': 1}

        code = self._code
        try:
            _send_code(email, code)
        except Exception:  # TODO: to clarify
            return {'error': 2}

        token = EmailUrl.add_email(email, password, code)
        return {
            'token': token
        }
