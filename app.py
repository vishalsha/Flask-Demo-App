
from flask import Flask
from flask import render_template
from flask import jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask App</h1>'

@app.route('/<name>')
def user(name):
	return '<h1>{}</h1>'.format(name)

@app.route('/target/<num>')
def getTargets(num):
	return 'List of top {} Ids are: {}'.format(num,[1111,2222,3333])

if __name__ == "__main__":
	app.run(host='localhost', port=5000)

	
#Query on browser using the routes, say.. http://localhost:5000/target/3
