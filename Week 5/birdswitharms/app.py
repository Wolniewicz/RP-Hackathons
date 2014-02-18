from flask import Flask
from flask import request

from flask import render_template
app = Flask(__name__)

@app.route('/')
def index ():
    return 'Hello World!'


@app.route('/search', methods=['POST', 'GET'])
def search():
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    temp = request.args.get('n', '')
    temp2 = request.args.get('query', '')
    if temp == '1' and temp2 == 'cardinal':
    	return '1 cardinal'
    if temp == '1':
	    return 'one result'
    else:
	    return 'nothing passed'


@app.route('/view')
def view():
	return 'View Page'



if __name__ == '__main__':
    app.run()