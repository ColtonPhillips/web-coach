from flask import render_template, request
import requests
import os
from neato import Prepender

def define(app):
	@app.route("/todo", methods = ['GET', 'POST'])
	def todo():
		full_path = os.path.join(app.root_path, "static", "todo.txt")
		# append new note
		if request.method == 'POST':	
			with Prepender(full_path) as todoFile:
				todoFile.write(request.form["idea"] + "\n===\n")
	
		#get existing notes
		todo = []
		with open(full_path,'r') as todoFile:
			todo = todoFile.read().split("===")

		# just added a note
		if request.method == 'POST':	
			return render_template("todo.html", todo=todo, form=request.form)
		else: 
			return render_template("todo.html", todo=todo)
