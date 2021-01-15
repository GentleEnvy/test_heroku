from typing import Any

from src.urls.crypt_url import CryptUrl


class Index(CryptUrl):
    @property
    def url(self) -> str:
        return '/'

    @property
    def methods(self) -> list[str]:
        return ['GET', 'POST']

    def reply(self, request: dict[str, Any]) -> dict[str, Any]:
        print(request)
        return request
