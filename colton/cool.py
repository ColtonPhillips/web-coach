from flask import render_template
import neato

def define(app):
	@app.route("/cool")
	def cool():
		neato.log_chince("randomlol")
		return render_template("cool.html")

