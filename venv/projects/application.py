
__version__ = '0.1'

from flask import Flask, url_for,render_template
app = Flask(__name__)
app.config['SECRET_KEY'] ='random'

from  controller import *

 
if __name__=='__main__':
    app.run(debug=True)