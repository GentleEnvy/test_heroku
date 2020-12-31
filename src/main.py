from src.app import app, run_configuration
from src.urls import init_urls

if __name__ == '__main__':
    init_urls(app)
    app.run(**run_configuration)
