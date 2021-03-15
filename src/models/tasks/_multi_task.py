from peewee import TextField
from playhouse.postgres_ext import ArrayField

from src.models.tasks.base_task import BaseTask

__all__ = ['MultiTask']


class MultiTask(BaseTask):
    rest_answers: tuple[str] = ArrayField(TextField)
    right_answers: tuple[str] = ArrayField(TextField)
