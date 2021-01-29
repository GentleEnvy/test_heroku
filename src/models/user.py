from __future__ import annotations

from typing import Optional, Any, final

from src.models.bases import Indexed


@final
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
            id_, password, avatar_url = cls.database.execute(
                f'''
                SELECT id, password, avatar_url
                    FROM "user"
                    WHERE email = %s;
                ''',
                [email]
            )[0]
        except IndexError:
            return None
        return cls.__create(id_, email, password, avatar_url)

    @classmethod
    def register(cls, email: str, password: str) -> User:
        res = cls.database.execute(
            f'''
            INSERT INTO "user" (
                email, password
            )
            VALUES (
                %s, %s
            )
            RETURNING id;
            ''',
            [email, password]
        )

        id_ = res[0][0]
        return cls.__create(id_, email, password)

    @classmethod
    def delete(cls, user: User):
        cls.database.execute(
            f'''
            DELETE FROM "user"
                WHERE id = %s;
            ''',
            [user.id]
        )

    @classmethod
    def __create(
            cls,
            id_: int, email: str, password: str,
            avatar_url: str = None
    ) -> User:
        return cls._create(id_, email, password, avatar_url)

    def __init__(self, id_: int, email: str, password: str, avatar_url: str):
        super().__init__(id_)
        self._email: str = email
        self._password: str = password
        self._avatar_url: str = avatar_url

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self.database.execute(
            f'''
            UPDATE "user"
            SET email = %s
                WHERE id = %s;
            ''',
            [email, self.id]
        )
        self._email = email

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> None:
        self.database.execute(
            f'''
            UPDATE "user"
            SET password = %s
                WHERE id = %s;
            ''',
            [password, self.id]
        )
        self._password = password

    @property
    def avatar_url(self) -> str:
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url: str) -> None:
        self.database.execute(
            f'''
            UPDATE "user"
            SET avatar_url = %s
                WHERE id = %s;
            ''',
            [avatar_url, self.id]
        )
        self._avatar_url = avatar_url

    @avatar_url.deleter
    def avatar_url(self) -> None:
        self.database.execute(
            f'''
            UPDATE "user"
            SET avatar_url = NULL
                WHERE id = %s;
            ''',
            [self.id]
        )
        self._avatar_url = None

    def serialize(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'avatar_url': self.avatar_url
        }
