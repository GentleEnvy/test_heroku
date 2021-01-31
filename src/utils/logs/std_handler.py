from logging import StreamHandler
import logging
from sys import stdout, stderr


class StdHandler(StreamHandler):
    def __init__(self, err_level: int = logging.WARNING):
        super().__init__(stdout)
        self._err_level = err_level

    def emit(self, record) -> None:
        if record.exc_info or record.levelno >= self._err_level:
            self.stream = stderr
        super().emit(record)
        self.stream = stdout
