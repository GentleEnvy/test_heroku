from __future__ import annotations

from abc import ABC
from typing import Final

from peewee import IntegerField

from src.models.bases.base_model import BaseModel

__all__ = ['Indexed']


class Indexed(BaseModel, ABC):
    id: Final[int] = IntegerField(primary_key=True)

    @classmethod
    def get_by_id(cls, id: int) -> Indexed:
        return super().get(id=id)
