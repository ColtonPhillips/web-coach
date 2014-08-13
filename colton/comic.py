from flask import render_template, request
import os, glob
 
def define(app):
	def comic_path(panel_id):
		return "/static/images/comic/" + str(panel_id) + ".jpg"
	app.jinja_env.globals.update(comic_path=comic_path)

	def comic_url(panel_id):
		return "http://www.coltonphillips.ca/comic/" + str(panel_id)
	app.jinja_env.globals.update(comic_url=comic_url)

	@app.route("/comic")
	@app.route("/comic/")
	@app.route("/comic/<panel_id>")
	def comic(panel_id=1):
		# Handle boundaries
		if (isinstance(panel_id,basestring)):
			if (not panel_id.isdigit()):
				panel_id = 1
		my_path = os.path.join(app.root_path, "static", "images", "comic")
		png_count = len(glob.glob1(my_path,"*.jpg"))
		if (int(panel_id) > png_count):
			panel_id = 1
		if (int(panel_id) < 1):
			panel_id = png_count	

		full_path = os.path.join(app.root_path, "static", "comic", "images", (str(panel_id) + ".jpg"))
		return render_template("comic.html", panel_id=panel_id)
		if(os.path.isfile(full_path)):
			return render_template("comic.html", panel_id=panel_id)
		else:
			return render_template("comic.html", panel_id=1)
