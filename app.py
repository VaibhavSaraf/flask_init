from flask import Flask
app = Flask(__name__)

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "hello world!"

@app.route('/hi')
def hi():
    return "hi"

if __name__=="__main__":
    app.run(host="127.0.0.1",port=80,debug=True)