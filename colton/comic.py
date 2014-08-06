from flask import render_template, request
import os

def define(app):
	@app.route("/comic")
	@app.route("/comic/<panel_id>")
	def comic(panel_id="1"):
		full_path = os.path.join(app.root_path, "static", "comic", (panel_id + ".png"))
		if(os.path.isfile(full_path)):
			return render_template("comic.html", panel_src="/static/comic/1.png")
		else:
			full_path = os.path.join(app.root_path, "static", "comic", "1.png")
			return render_template("comic.html", panel_src=full_path)
