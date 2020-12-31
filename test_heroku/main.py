from flask import request
from test_heroku.app import app

app = app.create_app()


@app.route('/')
def index():
    """ main func """
    return ''


if __name__ == '__main__':
    app.run(threaded=True, port=5000, debug=True)
