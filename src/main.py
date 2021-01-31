from logging import info

from src.app import app
from src.urls import init_urls
from src.utils import init_loggers


init_urls(app)
init_loggers()

info('program started')


if __name__ == '__main__':
    # on local
    # app.run(threaded=True)

    from src.utils import database

    print(database.execute('SELECT * FROM "unknow"'))
