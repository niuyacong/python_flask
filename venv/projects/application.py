
__version__ = '0.1'

from flask import Flask, url_for,render_template
app = Flask(__name__)
app.config['SECRET_KEY'] ='random'

from  controller import *
from configurations.config import configurations
import  mysql.connector
import json

# app.config['MYSQL_HOST']        = configurations.HOSTNAME
# app.config['MYSQL_USER']        = configurations.USERNAME
# app.config['MYSQL_PASSWORD']    = configurations.PASSWORD
# app.config['MYSQL_DB']          = configurations.DATABASE
# app.config['MYSQL_CURSORCLASS'] = configurations.CURSOR_CL

conn=mysql.connector.connect(user=configurations.USERNAME,password=configurations.PASSWORD,database=configurations.DATABASE)

@app.context_processor 
def admin_email():  
    with open(r"./static/data/menu.txt",'r') as load_f:
        load_dict = json.load(load_f) 
    return dict(email=load_dict) 

if __name__=='__main__':
    app.run(debug=True)