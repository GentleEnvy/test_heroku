from logging import exception
from typing import Final

from psycopg2 import connect
from psycopg2.extensions import connection, cursor

from src.utils.interfaces import Database

__all__ = ['PostgreSql']


class PostgreSql(Database):
    def __init__(self, database_url: str):
        self._connection: Final[connection] = connect(database_url)
        self._cursor: Final[cursor] = self._connection.cursor()

    def execute(self, query, values=None) -> tuple[tuple, ...]:
        try:
            self._cursor.execute(query=query, vars=values)
        except Exception:  # FIXME: check raises
            exception(f'{query = },\n{values = }')
        self._connection.commit()
        if self._cursor.pgresult_ptr is None:
            return ()
        return tuple(self._cursor.fetchall())
