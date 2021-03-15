from logging import Formatter, LogRecord
from textwrap import wrap
from typing import Final

from src.utils.functions import tab

__all__ = ['WrapFormatter']


def _wrap(text: str, max_length: int) -> str:
    wrapped_text_list = []
    if not text.startswith('\n'):
        text = '\n' + text
    for line in text.split('\n'):
        wrapped_text_list.extend(wrap(line, max_length))
    if text.startswith('\n'):
        return '\n' + '\n'.join(wrapped_text_list)
    return '\n'.join(wrapped_text_list)


class WrapFormatter(Formatter):
    _DEFAULT_MAX_LENGTH: Final[int] = 120

    # noinspection SpellCheckingInspection
    def __init__(
            self,
            fmt: str = None,
            datefmt: str = None,
            style: str = '%',
            validate: bool = True,
            max_length: int = _DEFAULT_MAX_LENGTH
    ):
        super().__init__(fmt, datefmt, style, validate)
        self._max_length = max_length

    def formatException(self, ei) -> str:
        if (formatted_exception := super().formatException(ei)).endswith('\n'):
            return tab('<<<\n' + tab(formatted_exception) + '>>>')
        return '<<<\n' + tab(formatted_exception) + '\n>>>'

    def format(self, record: LogRecord) -> str:
        formatted = super().format(record)
        if '\n' in record.message or len(formatted) > self._max_length:
            old_message = record.message
            record.message = tab(_wrap(record.message, self._max_length))
            formatted = super().format(record)
            record.message = old_message
        return formatted
