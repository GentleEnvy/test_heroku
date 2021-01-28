from typing import Any

from src.urls.bases import BaseUrl


class Echo(BaseUrl):
    @property
    def url(self) -> str:
        return '/echo'

    def get(self, request_json) -> dict[str, Any]:
        return request_json

    def post(self, request_json) -> dict[str, Any]:
        return request_json

    def put(self, request_json) -> dict[str, Any]:
        return request_json

    def delete(self, request_json) -> dict[str, Any]:
        return request_json
