import re
from logging import Filter, LogRecord

__all__ = ['ColorlessFilter']


class ColorlessFilter(Filter):
    def filter(self, record: LogRecord) -> bool:
        record.msg = re.sub('\\[\\d+m', '', record.msg)
        return super().filter(record)
