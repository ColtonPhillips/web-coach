from flask import render_template, request, make_response
import neato
from datetime import datetime
import MySQLdb

def define(app):
	@app.route("/cool", methods=['GET'])
	def cool_get():
		db = neato.MySQLdb_connect_secretly()
		cur = db.cursor()
		cur.execute("select * from coolness")
		return render_template("cool.html", chance=True)
		return str(cur.fetchall())
		day_of_year = str(datetime.now().month) + str(datetime.now().day)
		cool_date = request.cookies.get('day_of_year')
		if cool_date is None:
			resp = make_response(render_template("cool.html", chance=True))
			resp.set_cookie('day_of_year', day_of_year)
			return resp
		else:
			if (cool_date == day_of_year): 
				# You can only vote one time a day
				return render_template("cool.html", chance=False)
			else:
				resp = make_response(render_template("cool.html", chance=True))
				resp.set_cookie('day_of_year', day_of_year)
				return resp


	@app.route("/cool",methods=['POST'])
	def cool_post():
		return "shitstain"
		neato.log_chince("yay")
		db = neato.MySQLdb_connect_secretly()
		cur = db.cursor()
		cur.execute("select * from coolness")
		vals = cur.fetchall()
		neato.log_chince(vals)
		colton_coolness, brandon_coolness = vals[0],vals[1]
		my_query = "update `coolness` set `colton_coolness`={0}, `brandon_coolness`={1}".format(colton_coolness+1,brandon_coolness+1)
		cur.execute(my_query)
		cur.execute("select * from coolness")
		return str(cur.fetchall())
