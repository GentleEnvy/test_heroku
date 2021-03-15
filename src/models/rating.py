from typing import final

from peewee import ForeignKeyField, CompositeKey, IntegerField

from src.models.bases import BaseModel
from src.models.user import User
from src.models.subject import Subject

__all__ = ['Rating']


@final
class Rating(BaseModel):
    """
    CREATE TABLE rating (
    user_id Integer NOT NULL
        REFERENCES "user"
            ON DELETE CASCADE,
    subject_id Smallint NOT NULL
        REFERENCES subject
            ON DELETE CASCADE,
    elo Integer NOT NULL,

    PRIMARY KEY (user_id, subject_id)
    );
    """
    class Meta:
        primary_key = CompositeKey('user_id', 'subject_id')

    user_id = ForeignKeyField(User)
    subject_id = ForeignKeyField(Subject)
    elo = IntegerField()
