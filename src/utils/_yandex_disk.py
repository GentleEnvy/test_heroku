from logging import exception
from typing import Final

from yadisk import YaDisk
from yadisk.exceptions import PathExistsError

from src.utils.interfaces import FileBase

__all__ = ['YandexDisk']


class YandexDisk(FileBase):
    def __init__(self, token: str):
        self.ya_disk: Final[YaDisk] = YaDisk(
            token=token
        )
        if not self.ya_disk.check_token():
            raise ValueError('Yandex disk token is invalid')

    def upload(self, file, path) -> None:
        try:
            self.ya_disk.upload(file, path)
        except PathExistsError:
            raise FileExistsError
        except:  # FIXME: check raises
            exception(f'{file = },\n{path = }')
