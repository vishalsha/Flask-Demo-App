
from flask import Flask
from flask import render_template
from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1></h1>'

@app.route('/<name>')
def user(name):
	return '<h1>{}</h1>'.format(name)


if __name__ == "__main__":
	app.run(host='localhost', port=5000)

