import os
from flask import render_template

def define(app, gallery_name, route, image_folder):
	def gallery():
		pictures = []
		for image_file in os.listdir(image_folder):
			source = "/static/images/" + gallery_name + "/"  + image_file
			name, _ = os.path.splitext(image_file)
			pictures.append((name, source))

		return render_template(gallery_name+".html", pictures=pictures)

	app.add_url_rule(route, gallery_name, gallery)
