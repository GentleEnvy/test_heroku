import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello, dev brunch !'


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
