from typing import Any

from src.urls.base_url import BaseUrl


class Index(BaseUrl):
    @property
    def url(self) -> str:
        return '/'

    @property
    def methods(self) -> list[str]:
        return ['GET', 'POST']

    def reply(self, request: dict[str, Any]) -> dict[str, Any]:
        print(request)
        return request
