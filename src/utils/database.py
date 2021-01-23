from psycopg2 import connect
from psycopg2.extensions import connection, cursor

__all__ = ['Database']


class Database:
    """
    Util class for sending SQL queries to the database, TODO: more database functional
    """
    def __init__(self, database_url: str):
        self._connection: connection = connect(database_url)
        self._cursor: cursor = self._connection.cursor()

    def execute(self, query: str) -> list[tuple]:
        """
        :param query: SQL code
        :return: a list of requested tables in the form of tuples,
            if nothing was requested, an empty list is returned
        """
        self._cursor.execute(query=query)
        self._connection.commit()
        if self._cursor.pgresult_ptr is None:
            return []
        return self._cursor.fetchall()
