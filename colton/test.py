from flask import render_template, request
import os
from prepender import Prepender

def define(app):
	@app.route("/test", methods = ['GET', 'POST'])
	def test():
		# append new note
		if request.method == 'POST':	
			with Prepender(full_path) as notesFile:
				notesFile.write(request.form.note)
	
		#get existing notes
		notes = []
		full_path = os.path.join(app.root_path, "static", "notes.txt")
		with open(full_path,'r') as notesFile:
			notes = notesFile.read().split("===")

		# just added a note
		if request.method == 'POST':	
			return render_template("test.html", notes=notes, form=request.form)
		else: 
			return render_template("test.html", notes=notes)
"""
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
"""
