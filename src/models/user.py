from __future__ import annotations
from typing import Final

from src.models.base_model import BaseModel


class User(BaseModel):
    @classmethod
    def get(cls, id_: int) -> User:
        login, password = cls.database.execute(
            f'SELECT login, password'
            f'  FROM "user"'
            f'  WHERE id = {id_}'
        )
        return cls.__create(id_, login, password)

    @classmethod
    def register(cls, login: str, password: str) -> User:
        id_ = cls.database.execute(
            f'INSERT INTO "user" ('
            f'  login, password'
            f') VALUES ('
            f'  \'{login}\', \'{password}\''
            f') RETURNING id'
        )[0]
        return cls.__create(id_, login, password)

    @classmethod
    def delete(cls, user: User):
        cls.database.execute(
            f'DELETE FROM "user"'
            f'  WHERE id = {user.id}'
        )

    @classmethod
    def __create(cls, id_: int, login: str, password: str) -> User:
        return super()._create(id_, login, password)

    def __init__(self, id_: int, login: str, password: str):
        super().__init__(id_)
        self.login: Final[str] = login
        self.password: Final[str] = password
