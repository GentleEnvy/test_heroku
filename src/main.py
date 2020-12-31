import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World !'


print(__name__)
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
