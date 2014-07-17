from flask import render_template, request
import os
from neato import Prepender

def define(app):
	@app.route("/test", methods = ['GET', 'POST'])
	def test():
		full_path = os.path.join(app.root_path, "static", "notes.txt")
		# append new note
#		if request.method == 'POST':	
#			with Prepender(full_path) as notesFile:
#				pass
#				notesFile.write(str(request.form.note) + "\n===\n")
	
		#get existing notes
		notes = []
		with open(full_path,'r') as notesFile:
			notes = notesFile.read().split("===")
		if request.method == 'POST':
			pass
#			notes.append(request.form.note)

		# just added a note
		if request.method == 'POST':	
			return render_template("test.html", notes=notes, form=request.form)
		else: 
			return render_template("test.html", notes=notes)
