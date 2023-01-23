from app import app
@app.route('/')
def hello_world():
    return 'Hey ya, Im starting here'


@app.route('/')
def index():
    return 'Welcome to my Flask app!'


@app.route('/hello')
def hello():
    name = app.request.args.get('name')
    return f'Hello, {name}!'


@app.route('/add', app.methods['POST'])
def add():
    data = app.request.get_json()
    a = data['a']
    b = data['b']
    result = a + b
    return app.jsonify({'result': result})


if __name__ == '__main__':
    app.run()
