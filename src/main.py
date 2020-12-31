import flask


class MyApp(flask.Flask):

    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        print(f'run: {self.name = }')
        print(f'run: __name__: {__name__}')
        super().run(host, port, debug, load_dotenv, **options)


print(f'__name__ = {__name__}')
app = MyApp(__name__)
print(f'create app: {app.name}')


@app.route('/')
def index():
    return __name__


if __name__ == '__main__':
    print(f'running: {__name__}')
    app.run(threaded=True, port=5002)
