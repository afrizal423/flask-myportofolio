from flask import Flask, render_template

app = Flask(__name__,template_folder='templates')

from app import routes

from flask import Flask 

