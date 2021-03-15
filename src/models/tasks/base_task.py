from abc import ABC

from peewee import ForeignKeyField, SmallIntegerField, TextField

from src.models.bases import Indexed
from src.models.subject import Subject

__all__ = ['BaseTask']


class BaseTask(Indexed, ABC):
    subject_id: int = ForeignKeyField(Subject, Subject.id)
    number: int = SmallIntegerField()
    text: str = TextField()
