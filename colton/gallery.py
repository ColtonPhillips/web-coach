import os
from flask import render_template

def define(app, gallery_name, route, gallery_folder):
	def gallery():
		pictures = []
		full_path = os.path.join(app.root_path, "static", "images", gallery_folder)
		for image_file in os.listdir(full_path):
			source = "/static/images/" + gallery_folder + "/" + image_file
			name, _ = os.path.splitext(image_file)
			pictures.append((name, source))

		return render_template("gallery.html", pictures=pictures)

	app.add_url_rule(route, gallery_name, gallery)
