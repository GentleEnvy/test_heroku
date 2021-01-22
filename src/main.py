from src.app import app
from src.urls import init_urls

init_urls(app)

if __name__ == '__main__':
    # on local
    app.run(threaded=True)
