import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """ main func """
    return 'Hello, World !'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
