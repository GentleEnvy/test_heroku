import flask


class MyApp(flask.Flask):
    cache = set()

    def __getattribute__(self, item):
        result = super().__getattribute__(item)
        if item not in self.cache:
            print(f'getting attr: {item} -> {result}')
            self.cache.add(item)
        return result

    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        print(f'run: {self.name = }')
        print(f'run: __name__: {__name__}')
        super().run(host, port, debug, load_dotenv, **options)


print(f'__name__ = {__name__}')
app = MyApp(__name__)
print(f'create app: {app.name}')


@app.route('/')
def index():
    return app


if __name__ == '__main__':
    print(f'running: {__name__}')
    app.run(threaded=True, port=5002)
