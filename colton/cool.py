from flask import render_template
import neato

def define(app):
	@app.route("/cool")
	def cool():
		neato.log_chince("randomlol")
		from app import APP_ROOT_PATH
		return APP_ROOT_PATH
		return render_template("cool.html")

