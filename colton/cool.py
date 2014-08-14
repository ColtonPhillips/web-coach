from flask import render_template, request, make_response
import neato

def define(app):
	@app.route("/cool")
	def cool():
		meh = request.cookies.get('day_of_year')
#		resp = make_response(render_template("cool.html"))
#		resp.set_cookie('day_of_the_year', "today!")
#		return resp
		return meh
		return render_template("cool.html")

