'index module'
__author__ = 'nyc'


from application import app
from flask import render_template, request
from application import conn


@app.route('/index')
def index(name=None):
    return render_template('index.html')