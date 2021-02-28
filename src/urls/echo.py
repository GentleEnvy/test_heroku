from typing import Any

from src.urls.bases import IpSessionUrl


class Echo(IpSessionUrl):
    url = '/echo'

    def get(self, request_json) -> dict[str, Any]:
        return request_json

    def post(self, request_json) -> dict[str, Any]:
        return request_json

    def put(self, request_json) -> dict[str, Any]:
        return request_json

    def delete(self, request_json) -> dict[str, Any]:
        return request_json
