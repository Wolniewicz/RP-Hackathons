from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index ():
    name = request.args.get('name', '')
    return "Hello " + name
    #return render_template('home.html', name=name)


@app.route('/search', methods=['POST', 'GET'])
def search():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    search = request.args.get('n', '')
    bird = request.args.get('query', '')
    if search == '1' and bird == 'cardinal':
    	return '1 cardinal'
    	#return render_template('CHANGENAME.html')
    if search	 == '1':
	    return 'one result'
	    #return render_template('CHANGENAME.html')
    else:
	    return 'nothing passed'
	    #return render_template('CHANGENAME.html')


@app.route('/view')
@app.route('/view/<birdname>')
def view(birdname=None):
	return render_template('view.html', birdname=birdname)
   



if __name__ == '__main__':
    app.run()
