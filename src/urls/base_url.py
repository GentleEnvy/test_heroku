from typing import Union, AnyStr, final
from abc import ABC, ABCMeta, abstractmethod

from flask import (
    Flask, Response, Request,
    request as flask_request
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

        print(f'rule={self.url}, methods={self.methods}')

        @app.route(rule=self.url, methods=self.methods)
        def index() -> Response:
            return app.make_response(self.reply(flask_request))

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
