from flask import Flask,request
app = Flask(__name__)

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "world!"

@app.route('/hi')
def hi():
    return "hi"

@app.route('/bye')
def bye():
    retJson = {
        'Name':'Vaibhav',
        'Roll No.:':'31453'
    }
    return retJson

@app.route('/home', methods=['POST','GET'], defaults = {'name' : 'Default'})
@app.route('/home/<string:name>', methods = ['POST','GET'])
def home(name):
    return '<h1>Hello {}, You are in homepage now</h1>'.format(name)

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1> hi {}. you are from {}. you are on query page</h1> '.format(name,location)


if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)