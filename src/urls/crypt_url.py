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
from src.models import User

__all__ = ['CryptUrl', 'Connect']

_key_cache: dict[int, _Session] = {}


def _to_bytes(parameter: Any) -> bytes:
    try:
        return bytes(parameter)
    except TypeError:
        if isinstance(parameter, Iterable):
            return bytes(map(int, parameter))
    raise TypeError


class _Session:
    def __init__(self, key_server: PrivateKey):
        self.key_server: Final[PrivateKey] = key_server


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

    def reply(self, request: dict[str, Any]) -> dict[str, Any]:
        pass  # TODO
