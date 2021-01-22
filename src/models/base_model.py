from __future__ import annotations
from typing import Final
from abc import ABC

from src.utils.database import Database
from src.utils import database as util_database
from src.utils import MetaPrivateInit

__all__ = ['BaseModel']


class _MetaBaseModel(MetaPrivateInit, type(ABC)):
    pass


class BaseModel(ABC, metaclass=_MetaBaseModel):
    database: Database = util_database

    @classmethod
    def _create_model(cls, id_: int, *args, **kwargs):
        return cls._create(id_, *args, **kwargs)

    def __init__(self, id_: int):
        self.id: Final[int] = id_

    def __hash__(self):
        return self.id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False
