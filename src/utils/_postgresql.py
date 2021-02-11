from logging import exception
from typing import Final

from peewee import PostgresqlDatabase
from playhouse.db_url import connect
from psycopg2.extensions import cursor

from src.utils.interfaces import Database

__all__ = ['PostgreSql']


class PostgreSql(Database):
    def __init__(self, database_url: str):
        self._connection: Final[PostgresqlDatabase] = connect(database_url)
        self._cursor: Final[cursor] = self._connection.cursor()

    @property
    def connect(self):
        return self._connection

    def execute(self, query, values=None) -> tuple[tuple, ...]:
        try:
            self._cursor.execute(query=query, vars=values)
        except Exception:  # FIXME: check raises
            exception(f'{query = },\n{values = }')
            raise
        self._connection.commit()
        if self._cursor.pgresult_ptr is None:
            return ()
        return tuple(self._cursor.fetchall())
