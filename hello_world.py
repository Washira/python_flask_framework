from flask import Flask #import module
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world() : #create module expressing "Hello world"
  return "Hello World"

if __name__ == '__main__' :
  app.run()
