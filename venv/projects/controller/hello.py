
from application import app
from flask import render_template, request
from application import conn
import json
@app.route('/')
def index():
    return 'Hello World11!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login/')
def login():
    return 'The project page'

@app.route('/about')
def profile():
    return 'The about page'


@app.route('/test')
def test():
    cursor=conn.cursor()
    cursor.execute('insert into test(name) values(%s)',['niu'])
    conn.commit()
    print(cursor.rowcount)
    cursor.close()
    return 'success'


@app.route('/city')
def  insert_data():
    with open(r"resource/test.json",'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
    return 'success'