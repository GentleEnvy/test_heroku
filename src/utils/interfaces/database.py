from abc import ABC, abstractmethod

__all__ = ['Database']


class Database(ABC):
    @abstractmethod
    def execute(self, query: str) -> tuple[tuple, ...]:
        raise NotImplementedError
