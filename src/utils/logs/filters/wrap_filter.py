from logging import Filter, LogRecord

__all__ = ['WrapFilter']


class WrapFilter(Filter):
    def filter(self, record: LogRecord) -> bool:
        record.msg = record.msg.replace('\n', '\n\t')
        return super().filter(record)
