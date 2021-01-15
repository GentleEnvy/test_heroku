from psycopg2 import connect
# for typing
from psycopg2.extensions import connection, cursor

from src import DATABASE_URL


class Database:
    def __init__(self):
        self._connection: connection = connect(DATABASE_URL)
        self._cursor: cursor = self._connection.cursor()

    def execute(self, query: str) -> tuple:
        return self._cursor.execute(query=query)
