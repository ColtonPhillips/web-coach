from flask import render_template
import neato

def define(app):
	@app.route("/cool")
	def cool():
		return render_template("cool.html")

