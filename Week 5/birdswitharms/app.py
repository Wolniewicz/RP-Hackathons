from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return 'Hello World!'


@app.route('/search')
def resume():
	return 'Search Page'


@app.route('/view')
@app.route('/view/<birdname>')
def view(birdname=None):
	return render_template('view.html', birdname=birdname)
   



if __name__ == '__main__':
    app.run()
