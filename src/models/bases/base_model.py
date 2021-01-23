from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Final, Any

from src.utils import MetaPrivateInit, database as util_database
from src.utils.database import Database

__all__ = ['BaseModel']


class _MetaBaseModel(MetaPrivateInit, type(ABC)):
    pass


class BaseModel(ABC, metaclass=_MetaBaseModel):
    """
    TODO
    """
    database: Database = util_database

    @property
    @abstractmethod
    def primary_key(self) -> Any:
        raise NotImplementedError

    def __hash__(self):
        return self.primary_key

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.primary_key == other.primary_key
        return False

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self):
        return str(self)
