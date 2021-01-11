from typing import Union, AnyStr, final
from abc import ABC, ABCMeta, abstractmethod
from http import HTTPStatus

from flask import (
    Flask, Response, Request,
    request as flask_request,
    abort
)

__all__ = ['BaseUrl']


class _MetaBaseUrl(ABCMeta):
    __classes = set()

    @property
    def classes(cls) -> frozenset:
        return frozenset(cls.__classes)

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if ABC not in cls.__bases__:
            mcs.__classes.add(cls)
        return cls


class BaseUrl(ABC, metaclass=_MetaBaseUrl):
    def __init__(self, app: Flask):
        self.__app = app

        @app.route(rule=self.url, methods=self.methods)
        def index() -> Response:
            reply = self.reply(flask_request)
            resp = app.make_response(reply)
            resp.status_code = 200
            print(resp.__dict__)
            return resp

    @property
    @final
    def app(self) -> Flask:
        return self.__app

    @property
    @abstractmethod
    def url(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def methods(self) -> list[str]:
        """
        :return: list of literals GET, POST, PUT, DELETE
        """
        raise NotImplementedError

    @abstractmethod
    def reply(self, request: Request) -> Union[AnyStr, dict, tuple]:
        raise NotImplementedError
