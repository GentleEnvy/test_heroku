from __future__ import annotations

from typing import Optional, Any, final

from peewee import TextField

from src.models.bases import Indexed


@final
class User(Indexed):
    """
    CREATE TABLE "user" (
        name Serial NOT NULL
            PRIMARY KEY,
        email Text NOT NULL
            UNIQUE,
        password Text NOT NULL,\n
        avatar_url Text
            CHECK (avatar_url ~ 'https?://.+')
    );
    """
    email = TextField()
    password = TextField()
    avatar_url = TextField()

    @classmethod
    def get_by_id(cls, id) -> User:
        return super().get_by_id(id)

    @classmethod
    def get_by_email(cls, email: str) -> User:
        return super().get(email=email)

    @classmethod
    def create(cls, email: str, password: str, avatar_url: str = None) -> User:
        return super().create(email=email, password=password, avatar_url=avatar_url)


user = User.create(email='envy@mail.ru')
