from abc import ABC, abstractmethod

__all__ = ['Email']


class Email(ABC):
    @abstractmethod
    def send(self, message: str, to: str, subject: str = None) -> None:
        raise NotImplementedError
