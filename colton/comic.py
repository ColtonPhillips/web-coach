from flask import render_template, request
import os

def define(app):
	def comic_path(panel_id):
		return "/static/comic/" + panel_id + ".png"
 
	app.jinja_env.globals.update(comic_path=comic_path)

	@app.route("/comic")
	@app.route("/comic/")
	@app.route("/comic/<panel_id>")
	def comic(panel_id="1"):
		full_path = os.path.join(app.root_path, "static", "comic", (panel_id + ".png"))
		if(os.path.isfile(full_path)):
			return render_template("comic.html", panel_id=panel_id)
		else:
			return render_template("comic.html", panel_id=1)
