from abc import ABC, abstractmethod
from typing import Optional, Union

__all__ = ['Database']

_DatabaseTypes = Optional[Union[int, str, float, bool, bytes]]


class Database(ABC):
    """
    Util class for sending SQL queries to the database
    """
    @property
    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def execute(
            self, query: str,
            values: list[_DatabaseTypes] = None
    ) -> tuple[tuple, ...]:
        """
        :param query: SQL code
        :param values: values substituted in SQL code
        :return: a tuple of requested tables in the form of tuples,
            if nothing was requested, an empty tuple is returned
        """
        raise NotImplementedError
