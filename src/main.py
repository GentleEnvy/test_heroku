from src.app import app
from src.urls import init_urls

import logging

logFormatter = logging.Formatter(
    '///%(name)s: %(message)s///'
)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)

werkzeug = logging.getLogger('werkzeug')
werkzeug.addHandler(consoleHandler)
werkzeug.setLevel(logging.DEBUG)

# logFormatter = logging.Formatter(
#     '///[%(asctime)s] %(levelname)s in %(module)s: %(message)s///'
# )
#
# logger.setLevel(logging.CRITICAL)
#
# app.logger.handlers[0].setFormatter(logging.Formatter("%(message)s"))
#
# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(logFormatter)
# logger.addHandler(consoleHandler)

werkzeug.info('test werkzeug')

init_urls(app)


if __name__ == '__main__':
    # on local
    app.run(threaded=True)

    # import socket
    #
    # sock = socket.socket()
    # print(sock)
    # sock.bind(('localhost', 9090))
    # sock.listen(10)
    # print('listening')
    #
    # conn, addr = sock.accept()
    # print('connect: ', addr)
    #
    # while True:
    #     data = input('>>> ')
    #     conn.send(data.encode())
