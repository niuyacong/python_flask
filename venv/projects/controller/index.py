'index module'
__author__ = 'nyc'


from application import app
from flask import render_template, request
from application import conn


@app.route('/index')
def index(name=None):
    cursor=conn.cursor()
    cursor.execute("select id,title,code,`table` from tb_table")
    value=cursor.fetchall()
    conn.commit()
    conn.close()
    print('---------------')
    
    print(type(value))
    return render_template('index.html',data=value)