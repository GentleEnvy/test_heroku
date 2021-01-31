from typing import Any, Final

from flask import Response

from src.urls.bases import BaseUrl

__all__ = ['Index']


def _link_url(url: str) -> str:
    return f'&nbsp;&nbsp;<a href="{url}/documentation">{url}</a>'


class Index(BaseUrl):
    url: Final[str] = '/'

    def _make_response(self, response_json) -> Response:
        return self.app.make_response(
            f'''
            <p>To view the documentation: go to the `url` + '/documentation'</p>
            <hr>
            Urls:<br>
            {_link_url('/registration')} - user registration<br>
            {_link_url('/authorization')} - user authorization<br>
            {_link_url('/email')} - check the code from the email for registration<br>
            {_link_url('/user')} - get information about the user or delete his<br>
            {_link_url('/user/avatar')} - set the user's avatar
            '''
        )

    def get(self, request_json) -> dict[str, Any]:
        return {}
