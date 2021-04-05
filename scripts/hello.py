from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # return '<h1>Hello World!<h1/>'
    user_agent = request.headers.get('User-Agent')
    return '<h1>Bad Request<h1/>', 400

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
