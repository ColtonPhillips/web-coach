from flask import render_template
import neato

def define(app):
	@app.route("/cool")
	def cool():
		from app import APP_ROOT_PATH
		neato.log_chince("holy fucking shit it works:" + APP_ROOT_PATH)
		return render_template("cool.html")

