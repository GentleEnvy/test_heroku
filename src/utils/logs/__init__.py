import json
import logging
from logging import Logger, LogRecord
from logging.config import dictConfig

from src import ON_HOSTING
from src.utils.functions import get_path_to_src
from src.utils.logs._logs_drainer import LogsDrainer

__all__ = ['init_loggers']


class _CacheMessageLogRecord(LogRecord):
    def __init__(self, name, level, pathname, lineno,
                 msg, args, exc_info, func=None, sinfo=None):
        super().__init__(name, level, pathname, lineno, msg, args, exc_info, func, sinfo)
        self.message = super().getMessage()

    def getMessage(self) -> str:
        if self.message:
            return self.message
        self.message = super().getMessage()
        return self.message


logging.setLogRecordFactory(_CacheMessageLogRecord)


def _init_werkzeug(werkzeug: Logger):
    pass


def _init_gunicorn_access(gunicorn_access: Logger):
    pass


def _init_root(root: Logger):
    pass


_LOGGERS = {
    'werkzeug': _init_werkzeug,
    'gunicorn.access': _init_gunicorn_access,
    'root': _init_root
    # 'gunicorn.error'
}


def init_loggers() -> None:
    if ON_HOSTING:
        path_to_config = get_path_to_src() + '/utils/logs/prod_config.json'
    else:
        path_to_config = get_path_to_src() + '/utils/logs/dev_config.json'

    with open(path_to_config, 'r') as logs_config_json:
        logs_config = json.load(logs_config_json)

    dictConfig(logs_config)
    for logger_name, init_logger in _LOGGERS.items():
        logger = logging.getLogger(logger_name)
        init_logger(logger)

    if ON_HOSTING:
        LogsDrainer(
            path_to_logs=f'{get_path_to_src()}/utils/logs/logs.log'
        ).listen()
