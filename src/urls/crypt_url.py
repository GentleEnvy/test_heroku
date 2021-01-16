from __future__ import annotations
from typing import Any, Final, Iterable
from abc import ABC
from http import HTTPStatus
import json

from flask import Flask, Request, send_file
from rsa import PublicKey, PrivateKey
import rsa
from cryptography.fernet import Fernet

from src.urls.base_url import BaseUrl
from src.urls.exceptions import HTTPException, NoParameterException
from src.utils import MetaPrivateConstructor
from src.models import User

__all__ = ['CryptUrl', 'Connect']

_user_session: dict[int, _Session] = {}
_ip_session: dict[str, _Session] = {}


def _to_bytes(parameter: Any) -> bytes:
    try:
        return bytes(parameter)
    except TypeError:
        if isinstance(parameter, Iterable):
            return bytes(map(int, parameter))
    raise TypeError


class _Session:
    def __init__(self, user_key: int):
        self.public_user_key: Final[PublicKey] = PublicKey(
            user_key,
            rsa.key.DEFAULT_EXPONENT
        )
        server_keys = rsa.newkeys(512)
        self.private_server_key: Final[PublicKey] = server_keys[0]
        self.public_server_key: Final[PrivateKey] = server_keys[1]


class CryptUrl(BaseUrl, ABC):
    @staticmethod
    def _parse_request(request: Request) -> dict[str, Any]:
        parsed_request: dict[str, Any] = BaseUrl._parse_request(request)

        # try:
        #     user_id: int = int(parsed_request['id'])
        # except KeyError:
        #     raise NoParameterException('id')
        # except TypeError:
        #     raise HTTPException(
        #         HTTPStatus.BAD_REQUEST,
        #         '`id` must be <int>'
        #     )
        try:
            key_bytes: bytes = _to_bytes(parsed_request['key'])
        except KeyError:
            raise NoParameterException('key')
        except TypeError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                '`key` must be <bytes> or <list[int]>'
            )
        try:
            query_bytes: bytes = _to_bytes(parsed_request['query'])
        except KeyError:
            raise NoParameterException('query')
        except TypeError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                '`query` must be <bytes> or <list[int]>'
            )

        return {
            'key': str(key_bytes),
            'query': str(query_bytes)
        }


class Connect(BaseUrl):
    @property
    def url(self) -> str:
        return '/connect'

    @property
    def methods(self) -> list[str]:
        return ['POST']

    @staticmethod
    def _parse_request(request: Request) -> dict[str, Any]:
        parsed_request: dict[str, Any] = BaseUrl._parse_request(request)
        print(f'{parsed_request = }')  # TODO: log

        try:
            user_key: int = int(parsed_request['key'])
        except KeyError:
            raise NoParameterException('key')
        except ValueError:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST,
                '`key` must be <int>'
            )
        try:
            ip: str = request.environ['HTTP_X_FORWARDED_FOR']
        except KeyError:
            raise HTTPException(HTTPStatus.UNAUTHORIZED, 'No IP')  # TODO

        return {
            'key': user_key,
            'ip': ip
        }

    def reply(self, request: dict[str, Any]) -> dict[str, Any]:
        session = _Session(request['key'])
        _ip_session[request['ip']] = session
        return {
            'key': session.public_server_key.n
        }
