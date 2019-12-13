from flask import Flask, escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<name>')
def hello(name):
    return 'Hello, {}!'.format(escape(name))