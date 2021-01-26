from src.app import app
from src.urls import init_urls

from src.models import User
import time

t = time.time()
user = User.get('envy15@mail.ru')
print(user)
print(time.time() - t)
t = time.time()
print(user.avatar_url)
print(time.time() - t)

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
