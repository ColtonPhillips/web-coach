from flask import render_template, request, make_response
import neato
from datetime import datetime

def define(app):
	@app.route("/cool")
	def cool():
		return "oh god i just wish things would load faster"
		# Lazy, not pefect way to solve it
		cool_date = request.cookies.get('day_of_month')
		neato.chince_log(cool_date)
		return "test"
		if cool_date is None:
			resp = make_response(render_template("cool.html"))
			resp.set_cookie('day_of_month', datetime.now().month)
			return resp
		else:
			if (cool_date == datetime.now().month):
				return "same day"
			else:
				return "different day"
