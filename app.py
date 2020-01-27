from flask import Flask,request,jsonify,url_for,redirect,session

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'THIS IS A SECRET'

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "world!"

@app.route('/hi')
def hi():
    session.pop('name',None)
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
    session['name'] = name
    return '<h1>Hello {}, You are in homepage now</h1>'.format(name)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession'
    return jsonify({'key' : 'value', 'listkey' : [1,2,3], 'name' : name})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1> hi {}. you are from {}. you are on query page</h1> '.format(name,location)

@app.route('/theform', methods = ['GET','POST'])
def theform():
    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                      <input type="text" name="name">
                      <input type="text" name="location">
                      <input type="submit">
                  </form>'''
    else:
        name = request.form['name']
        location = request.form['location']
        # return 'hello {}. You are from {}. You have submitted the form successfully!'.format(name,location)

        return redirect(url_for('home',name=name,location=location))
'''
@app.route('/process',methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return 'hello {}. You are from {}. You have submitted the form successfully!'.format(name,location)
'''
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name  = data['name']
    location = data['location']
    randamlist = data['randamlist']
    return jsonify({'result':'success!', 'name' : name, 'location' : location, 'randamlist' : randamlist[1] })

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000)