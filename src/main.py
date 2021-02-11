from logging import info

from src.app import app
from src.urls import init_urls
from src.utils import init_loggers

init_loggers()
init_urls(app)

info('Server started !')

if __name__ == '__main__':
    # on local
    # app.run(threaded=True)

    from src.models import User

    u = User.create(email='envy15 mail.ru', password='abc')
    print(u)
