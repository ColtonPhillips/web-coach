from flask import render_template, request, make_response
import neato
from datetime import datetime

def define(app):
	@app.route("/cool")
	def cool():
		day_of_year = str(datetime.now().month) + str(datetime.now().day)
		cool_date = request.cookies.get('day_of_year')
		if cool_date is None:
			resp = make_response(render_template("cool.html"))
			resp.set_cookie('day_of_year', day_of_year)
			return resp
		else:
			if (cool_date == day_of_year): 
				# You can only vote one time a day
				return "same day"
			else:
				return "different day"
