from flask import render_template, request, make_response
import neato
from datetime import datetime

def define(app):
	@app.route("/cool")
	def cool():
		# Lazy, not pefect way to solve it
		cool_date = request.cookies.get('day_of_month')
		if cool_date is None:
			snoog = str(cool_date) + str('a')
			neato.log_chince(snoog)
			resp = make_response(render_template("cool.html"))
			resp.set_cookie('day_of_month', str(datetime.now().month))
			return resp
		else:
			if (cool_date == datetime.now().month):
				snoog = str(cool_date) + str('b')
				neato.log_chince(snoog)
				return "same day"
			else:
				snoog = str(cool_date) + str('c')
				neato.log_chince(snoog)
				return "different day"
