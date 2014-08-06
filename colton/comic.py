from flask import render_template, request
import os

def define(app):
	@app.route("/comic")
	@app.route("/comic/<panel_id>")
	def comic(panel_id="1"):
		return render_template("comic.html", panel_id=panel_id)
