from flask import Flask
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
"""
all communications between server between server/server, server/browser, browser/browser
it is in "TEXT" TC
return Image
[
    123 125 126 127
    124 125 126 127
]


"""

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000,debug=True)