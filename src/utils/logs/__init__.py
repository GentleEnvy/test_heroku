import json
import logging
from logging import LogRecord
from logging.config import dictConfig
from typing import Optional

from src import ON_HOSTING
from src.utils.functions import get_path_to_src
from src.utils.logs._logs_drainer import LogsDrainer

__all__ = ['init_loggers']


class _CacheMessageLogRecord(LogRecord):
    # noinspection SpellCheckingInspection
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__message: Optional[str] = None

    def getMessage(self) -> str:
        if self.__message:
            return self.__message
        self.__cache_message(super().getMessage())
        return self.__message

    @property
    def message(self) -> str:
        return self.getMessage()

    @message.setter
    def message(self, message: str):
        self.__cache_message(message)

    def __cache_message(self, message: str) -> None:
        self.__message = message
        self.__dict__['message'] = message


logging.setLogRecordFactory(_CacheMessageLogRecord)


def init_loggers() -> None:
    path_to_config = f'{get_path_to_src()}' \
                     f'/utils/logs/{"prod" if ON_HOSTING else "dev"}_config.json'
    with open(path_to_config, 'r') as logs_config_json:
        logs_config = json.load(logs_config_json)
    dictConfig(logs_config)

    if ON_HOSTING:
        LogsDrainer(f'{get_path_to_src()}/utils/logs/logs.log').listen()
