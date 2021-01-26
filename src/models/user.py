from __future__ import annotations

from typing import Final, Optional

from src.models.bases import Indexed


class User(Indexed):
    """
    CREATE TABLE "user" (
        id Serial
            PRIMARY KEY,
        email Varchar(100)
            UNIQUE NOT NULL,
        password Varchar(100) NOT NULL,
        avatar_url Varchar(2000)
            CHECK (avatar_url ~ 'https?://.+')
    );
    """
    @classmethod
    def get(cls, email: str) -> Optional[User]:
        try:
            id_, password = cls.database.execute(
                f'''
                SELECT
                    id,
                    password
                    FROM
                        "user"
                    WHERE
                        email = '{email}';
                '''
            )[0]
        except IndexError:
            return None
        return cls.__create(id_, email, password)

    @classmethod
    def register(cls, email: str, password: str) -> User:
        res = cls.database.execute(
            f'''
            INSERT
                INTO "user" (
                    email,
                    password
                )
                VALUES (
                    '{email}',
                    '{password}'
                )
            RETURNING id;
            '''
        )

        id_ = res[0][0]
        return cls.__create(id_, email, password)

    @classmethod
    def delete(cls, user: User):
        cls.database.execute(
            f'''
            DELETE
                FROM
                    "user"
                WHERE
                    id = {user.id};
            '''
        )

    @classmethod
    def __create(cls, id_: int, email: str, password: str) -> User:
        return cls._create(id_, email, password)

    def __init__(self, id_: int, email: str, password: str):
        super().__init__(id_)
        self.email: Final[str] = email
        self.password: Final[str] = password

    @property
    def avatar_url(self) -> str:
        return self.database.execute(
            f'''
            SELECT avatar_url
                FROM "user" WHERE id = {self.id};
            '''
        )[0][0]
