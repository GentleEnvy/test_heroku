from typing import Any

from flask import Response

from src.urls.bases import BaseUrl

__all__ = ['Index']


class Index(BaseUrl):
    @property
    def url(self) -> str:
        return '/'

    def _make_response(self, response_json: dict[str, Any]) -> Response:
        return self.app.make_response(
            '''
            <p>To view the documentation: go to the `url` + '/documentation'</p>
            <hr>
            Urls:<br>
            &nbsp;&nbsp;/registration - user registration<br>
            &nbsp;&nbsp;/authorization - user authorization<br>
            &nbsp;&nbsp;/email - check the code from the email for registration<br>
            &nbsp;&nbsp;/user - get information about the user or delete his
            '''
        )

    def get(self, request_json: dict[str, Any]) -> dict[str, Any]:
        return {}
