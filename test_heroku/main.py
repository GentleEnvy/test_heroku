import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """ main """
    return 'Hello, dev brunch !'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
