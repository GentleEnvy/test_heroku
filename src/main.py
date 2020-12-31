import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World !'


if __name__ == '__main__':
    print(f'running: {__name__}')
    app.run(threaded=True, port=5000)
