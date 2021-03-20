import json
import logging
from logging import LogRecord
from logging.config import dictConfig

from src import ON_HOSTING
from src.utils.functions import get_path_to_src
from src.utils.logs._logs_drainer import LogsDrainer

__all__ = ['init_loggers']


class _CacheMessageLogRecord(LogRecord):
    # noinspection SpellCheckingInspection
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__message: str = super().getMessage()

    def getMessage(self) -> str:
        if self.__message:
            return self.__message
        self.__message = super().getMessage()
        return self.__message


logging.setLogRecordFactory(_CacheMessageLogRecord)


def init_loggers() -> None:
    path_to_config = f'{get_path_to_src()}' \
                     f'/utils/logs/{"prod" if ON_HOSTING else "dev"}_config.json'
    with open(path_to_config, 'r') as logs_config_json:
        logs_config = json.load(logs_config_json)
    dictConfig(logs_config)

    if ON_HOSTING:
        LogsDrainer(f'{get_path_to_src()}/utils/logs/logs.log').listen()
