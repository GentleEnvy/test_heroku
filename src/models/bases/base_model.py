from __future__ import annotations

from abc import ABC
from typing import Any

from peewee import Model
from playhouse.shortcuts import model_to_dict

from src.utils import database as util_database

__all__ = ['BaseModel']


class _MetaBaseModel(type(Model), type(ABC)):
    pass


class BaseModel(Model, ABC, metaclass=_MetaBaseModel):
    """
    Base class for database models. Any model does not have a public __init__
    """
    class Meta:
        database = util_database.connect

    @staticmethod
    def execute(query, values=None) -> tuple[tuple, ...]:
        return util_database.execute(query, values)

    def serialize(self) -> dict[str, Any]:
        return model_to_dict(self)

    def __str__(self) -> str:
        return str(self.serialize())

    def __repr__(self):
        return str(self)


id = 5
BaseModel.execute(
    f'''
    SELECT * from "user" WHERE id = %s AND email = %s
    ''',
    [id, 'sas']
)
