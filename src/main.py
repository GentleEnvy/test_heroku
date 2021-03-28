from logging import info

from src.app import app
from src.urls import init_urls
from src.utils.logs import init_loggers

init_loggers()
init_urls(app)

info('Server started !')

from src.utils import database

database.execute('jjlsdjlsdkfjljdslfsjflkdfjslkfjslkfjldkjsflj lsdjf ljdlsdjlfdjslsdjfldjflsdjflsjflsdjfdlsfjsdlkfj dsfj slkjdlkjlskfjdslkfjsdlkfdjsflksjflkdsj lkdsjfd lskjsdl kjlksj sdlkjdslkdjslkdsjlksdfjldskfjsdlkfjsdlkfsdjlfk sdjlksdjf lkdsjlkds fjdlsk')

if __name__ == '__main__':
    app.run(threaded=True)
