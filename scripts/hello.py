from flask import (
    Flask, request, make_response, redirect, abort, render_template,
    )
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('templates/index.html', name=name)

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello, {}</h1>'.format(user.name)
