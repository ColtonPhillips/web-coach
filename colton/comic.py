from flask import render_template, request
import os

def define(app):
	@app.route("/comic")
	@app.route("/comic/")
	@app.route("/comic/<panel_id>")
	def comic(panel_id=1):
		full_path = os.path.join(app.root_path, "static", "comic", (str(panel_id) + ".png"))
		return render_template("boiler.html",shit=full_path)
		if(os.path.isfile(full_path)):
			return render_template("comic.html", panel_id=panel_id)
		else:
			return render_template("comic.html", panel_id=1)
