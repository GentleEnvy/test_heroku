import json
import logging
from logging import Logger
from logging.config import dictConfig

from src import ON_HOSTING
from src.utils import get_path_to_src
from src.utils.logs.filters import WrapFilter

__all__ = ['init_loggers']


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
