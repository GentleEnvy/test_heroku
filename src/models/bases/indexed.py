from abc import ABC
from typing import Final

from src.models.bases.base_model import BaseModel

__all__ = ['Indexed']


class Indexed(BaseModel, ABC):
    def __init__(self, id_: int):
        self.id: Final[int] = id_

    @property
    def primary_key(self) -> int:
        return self.id
