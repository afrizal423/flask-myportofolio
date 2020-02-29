from app import app
from flask import render_template, g
import flask as a
from platform import python_version
import time


@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

@app.route('/')
def index():
    user = a.__version__
    versi = {
        'flask': a.__version__,
        'python': python_version()
        }
    return render_template('bio.html',versi=versi)

@app.route('/home/<name>')  

def home(name):  
   return 'Hello %s!' % name
