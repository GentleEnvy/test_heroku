from flask import Flask

from src.app import run_configuration
from src.urls import init_urls

# init_urls(app)

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world !'


app.run()
