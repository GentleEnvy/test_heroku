import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """ Main function """
    return 'Hello, World !'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
