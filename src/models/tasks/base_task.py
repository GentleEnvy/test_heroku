from abc import ABC

from peewee import ForeignKeyField, SmallIntegerField, TextField

from src.models._subject import Subject
from src.models.base_models import IndexedModel

__all__ = ['BaseTask']


class BaseTask(IndexedModel, ABC):
    subject_id: int = ForeignKeyField(Subject, Subject.id)
    number: int = SmallIntegerField()
    text: str = TextField()
