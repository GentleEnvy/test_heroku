import flask

print(f'__name__ = {__name__}')
app = flask.Flask(__name__)
print(f'create app: {app.name}')


@app.route('/')
def index():
    return __name__


if __name__ == '__main__':
    print(f'running: {__name__}')
    app.run(threaded=True, port=5000)
