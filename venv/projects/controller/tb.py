'tb module'
__author__ = 'nyc'


from application import app
from flask import render_template, request
from application import conn


@app.route('/tb/delete', methods=['GET'])
def delete():
    id = request.args.get('id')
    print('................')
    print(id)
    cursor=conn.cursor()
    cursor.execute("delete from tb_table where id=%s",[id])
    row=cursor.rowcount
    conn.commit()
    cursor.close()
    return str(row)