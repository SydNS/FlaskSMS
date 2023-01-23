from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hey ya, Im starting here'


if __name__ == '__main__':
    app.run()
