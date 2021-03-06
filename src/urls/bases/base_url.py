import json
from abc import ABC, abstractmethod
from http import HTTPStatus
from logging import error, exception, info, warning
from typing import Any, Union, Final

from flask import Flask, Request, Response, request as flask_request

from src.urls.exceptions import HTTPException, NoParameterException

__all__ = ['BaseUrl']


class BaseUrl(ABC):
    def __init__(self, app: Flask):
        """
        Automatically adds a url to the app and documentation at the address
            <self.url>/documentation taken from __doc__ current class
        """
        self.app: Final[Flask] = app

        def index() -> Response:
            response: Request
            # noinspection PyBroadException
            try:
                request = flask_request
                info(f'{self.__class__.__name__}: request = {request.__dict__}')
                request_json = self._parse_request(request)
                info(f'{self.__class__.__name__}: {request_json = }')

                method = request.method.upper()
                if method == 'GET':
                    response_json = self.get(request_json)
                elif method == 'POST':
                    response_json = self.post(request_json)
                elif method == 'PUT':
                    response_json = self.put(request_json)
                elif method == 'DELETE':
                    response_json = self.delete(request_json)
                else:
                    warning(f'{self.__class__.__name__}: method {method} not allowed')
                    raise HTTPException(HTTPStatus.METHOD_NOT_ALLOWED)

                info(f'{self.__class__.__name__}: {response_json = }')
                response = self._make_response(response_json)
            except HTTPException as http_exception:
                warning(f'{self.__class__.__name__}: {http_exception = }')
                response = self._make_error_response(http_exception)
            except:  # FIXME: check raises
                exception(f'{self.__class__.__name__}')
                response = self._make_error_response()
            return response

        try:
            app.add_url_rule(
                rule=self.url,
                endpoint=self.__class__.__name__,
                view_func=index,
                methods=['GET', 'POST', 'PUT', 'DELETE']
            )
        except AssertionError as e:
            exception(f'{self.__class__.__name__}: repeat call __init__')
            raise e

        self.__create_documentation()
        info(f'{self.__class__.__name__} ({self.url}) inited')

    def __create_documentation(self) -> None:
        class_doc = self.__class__.__doc__
        if class_doc:
            # TODO: html doc
            class_doc = class_doc.replace('<', '&lt;')
            class_doc = class_doc.replace('>', '&gt;')
            class_doc = class_doc.replace('//', '<')
            class_doc = class_doc.replace(r'\\', '>')
            class_doc = class_doc.replace('\n    ', '<br>')
            class_doc = class_doc.replace(' ', '&nbsp;')

            def documentation() -> Response:
                return self.app.make_response(class_doc)

            self.app.add_url_rule(
                rule=self.url + '/documentation',
                endpoint=self.__class__.__name__ + '/Documentation',
                view_func=documentation,
                methods=['GET']
            )

    def _parse_request(self, request: Request) -> dict[str, Any]:
        """
        :param request: current http request
        :return: JSON parsed from request.data or request.form | request.args
        :raises HTTPException: if decoding to utf-8 or deserializing to JSON failed
        """
        try:
            if request.data:
                return json.loads(request.data.decode('utf-8'))
            return request.form | request.args
        except UnicodeDecodeError:
            raise HTTPException(HTTPStatus.BAD_REQUEST, 'The encoding must be UTF-8')
        except json.JSONDecodeError:
            raise HTTPException(HTTPStatus.BAD_REQUEST, 'Bad JSON')

    def _make_response(self, response_json: dict[str, Any]) -> Response:
        """
        :param response_json: server response in JSON format
        :return: server's final response
        """
        return self.app.make_response(json.dumps(response_json))

    def _make_error_response(
            self,
            http_exception: HTTPException = HTTPException()
    ) -> Response:
        """
        :param http_exception: the exception that occurred.
            Default: INTERNAL_SERVER_ERROR (500)
        :return: server's final response to the error
        """
        response: Response = self.app.make_response(str(http_exception))
        response.status_code = http_exception.http_status.value
        return response

    @property
    @abstractmethod
    def url(self) -> str:
        """
        :return: rule starting with '/'
        """
        raise NotImplementedError

    def get(self, request_json: dict[str, Any]) -> dict[str, Any]:
        """
        :param request_json: current http request in JSON format
        :return: GET method response
        """
        raise HTTPException(HTTPStatus.METHOD_NOT_ALLOWED)

    def post(self, request_json: dict[str, Any]) -> dict[str, Any]:
        """
        :param request_json: current http request in JSON format
        :return: POST method response
        """
        raise HTTPException(HTTPStatus.METHOD_NOT_ALLOWED)

    def put(self, request_json: dict[str, Any]) -> dict[str, Any]:
        """
        :param request_json: current http request in JSON format
        :return: PUT method response
        """
        raise HTTPException(HTTPStatus.METHOD_NOT_ALLOWED)

    def delete(self, request_json: dict[str, Any]) -> dict[str, Any]:
        """
        :param request_json: current http request in JSON format
        :return: DELETE method response
        """
        raise HTTPException(HTTPStatus.METHOD_NOT_ALLOWED)

    @staticmethod
    def get_value(
            request_json: dict[str, Any],
            name_parameter: str
    ) -> Union[int, str, bool, dict, list]:
        """
        :return: a required parameter in the request_json
        :raises NoParameterException: if name_parameter key not in request_json
        """
        try:
            return request_json[name_parameter]
        except KeyError:
            raise NoParameterException(name_parameter)
