from flask import Flask
app = Flask(__name__)

@app.route('/')
def index ():
    return 'Hello World!'


@app.route('/search')
def resume():
	return 'Search Page'


@app.route('/view')
def view():
	return 'View Page'



if __name__ == '__main__':
    app.run()