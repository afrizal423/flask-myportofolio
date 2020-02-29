import pymysql
from app import app
from app.db_config import mysql
from flask import render_template, g
import flask as a
from platform import python_version
import time
from flaskext.mysql import MySQL
from flask import jsonify
from flask import flash, request

# dipindahkan ke db_config

# mysql = MySQL()
 
# # MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'if17'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

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

@app.route('/mahasiswaif17')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM mahasiswa")
		rows = cursor.fetchall()
		message = {
        		'status': 'ok',
       			'response': rows
    		}
		resp = jsonify(message)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/mahasiswaif17/<int:npm>')
def carimhs(npm):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM mahasiswa where npm=%s",npm)
		rows = cursor.fetchall()
		message = {
        		'status': 'ok',
       			'response': rows
    		}
		resp = jsonify(message)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		