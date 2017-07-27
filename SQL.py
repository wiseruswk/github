# coding: utf - 8

import MySQLdb

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)  # insert Myfile to app

def shutdown_server():      #make func
    func = request.environ.get('werkzeug.server.shutdown')      #for shutdown flask
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')

def shutdown():     #http://localhost:8888/shutdown
    shutdown_server()
    return 'Server shutting down....'

@app.route('/delete')

def delete():
	db = MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	try:
		cur.execute("delete from EMP where ename='Lee'")
		cur.execute("select * from EMP")
		db.commit()
	except:
		db.rollback()
		return "fail delete"
	row = cur.fetchall()
	templateData = {'data' : row}
	return render_template('test2.html',**templateData)

	cur.close()
	db.close()	

@app.route('/')
def Start():
    
    return 'Start DATA......'

@app.route('/insert')
def insert():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    try:
    	cur.execute("insert into EMP(ename)values('Lee')")
    	cur.execute("select * from EMP")
    	db.commit()
    except:
	db.rollback()
	return 'fail the insert columns'
    row = cur.fetchall()

    templateData = {'data' : row}  #row = [][]
    return render_template('test2.html',**templateData)

    cur.close()
    db.close()


@app.route('/select')
def hello():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    cur.execute("select empno,ename,job,mgr,hiredate,sal,comm,deptno from EMP")
    row = cur.fetchall()

    templateData = {'data' : row}  #row = [][]
    return render_template('test2.html',**templateData)

    cur.close()
    db.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
