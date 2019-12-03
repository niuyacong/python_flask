
__version__ = '0.1'

from flask import Flask, url_for,render_template
app = Flask('projects')
app.config['SECRET_KEY'] ='random'

import projects.controller