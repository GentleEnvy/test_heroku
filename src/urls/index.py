from flask import Request

from .base_url import BaseUrl


class Index(BaseUrl):
    @property
    def url(self) -> str:
        return '/'

    @property
    def methods(self) -> list[str]:
        if self.app.debug:
            return ['GET', 'POST']
        return ['POST']

    def reply(self, request: Request) -> dict:
        # TODO: to implements the logic
        response = {
            'form': request.form,
            'args': request.args,
            'data': request.data
        }
        print(response)
        return response
