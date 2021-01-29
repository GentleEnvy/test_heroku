from threading import Thread
from time import sleep

from src.utils import get_path_to_src


def _print_logs():
    path_to_logs = get_path_to_src() + '/logs.log'
    with open(path_to_logs, 'r') as logs:
        print('logs: <<<', logs.read(), '>>>')
    sleep(30)


def print_logs():
    Thread(target=_print_logs, daemon=True).start()
