from typing import Any

from src.urls.bases import IpSessionUrl


class Echo(IpSessionUrl):
    @property
    def url(self) -> str:
        return '/echo'

    def _get(self, request_json, session) -> dict[str, Any]:
        return request_json

    def _post(self, request_json, session) -> dict[str, Any]:
        return request_json

    def _put(self, request_json, session) -> dict[str, Any]:
        return request_json

    def _delete(self, request_json, session) -> dict[str, Any]:
        return request_json
