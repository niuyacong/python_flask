'test module'
__author__ = 'nyc'


from application import app
from flask import render_template, request
from application import conn
import json


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

# 省市县的json数据（来源：weui），导入到数据库中
@app.route('/city')
def  insert_data():
    with open(r"resource/test.json",'r') as load_f:
        load_dict = json.load(load_f)
        cursor=conn.cursor()
        for prov in load_dict:
            cursor.execute('insert into tb_province(provid,provname,state) values(%s,%s,\'1\')',[prov["code"],prov["name"]])
            if len(prov["sub"])>0:
                for city in prov["sub"]:
                    cursor.execute('insert into tb_city(cityid,cityname,provid,provname,state) values(%s,%s,%s,%s,\'1\')',[city["code"],city["name"],prov["code"],prov["name"]])
                    if 'sub' in city and len(city["sub"])>0:
                        for country in city["sub"]:
                            cursor.execute('insert into tb_county(countyid,countyname,cityid,cityname,state) values(%s,%s,%s,%s,\'1\')',[country["code"],country["name"],city["code"],city["name"]])  
        conn.commit()
        cursor.close()
    return 'success'