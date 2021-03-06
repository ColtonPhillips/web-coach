import os, random
from flask import render_template

def define(app):
	@app.route("/logo")
	def logo():
		pictures = []
		full_path = os.path.join(app.root_path, "static", "images", "logo")
		for image_file in os.listdir(full_path):
			source = "/static/images/logo/" + image_file
			pictures.append(source)

		random.shuffle(pictures)
		return render_template("logo.html", pictures=pictures)
