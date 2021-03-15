from __future__ import annotations

from typing import final

from peewee import TextField

from src.models.base_models import IndexedModel, BaseModelEnum

__all__ = ['Subject']


@final
class Subject(IndexedModel, BaseModelEnum):
    """
    CREATE TABLE subject (
        name Smallint
            PRIMARY KEY,
        name Text NOT NULL
            UNIQUE
            CHECK (name != '')
    );
    """
    MATHEMATICS: Subject
    RUSSIAN_LANGUAGE: Subject

    @classmethod
    def _init_static(cls):
        cls.RUSSIAN_LANGUAGE = cls.get(id=1)
        cls.MATHEMATICS = cls.get(id=2)

    name: str = TextField()

    @classmethod
    def get_by_id(cls, id) -> Subject:
        return super().get_by_id(id)

    @classmethod
    def get_by_name(cls, name: str) -> Subject:
        return super().get(name=name)

    def delete_instance(self, recursive=False, delete_nullable=False):
        raise NotImplementedError
