from flask import render_template, request
import requests
import os
from neato import Prepender

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v2/sandboxb161ba3bb2314de2805f53614cfa0e1d.mailgun.org/messages",
		auth=("api", "key-844od-esiggre7cm8oju8walodfqkn26"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxb161ba3bb2314de2805f53614cfa0e1d.mailgun.org>",
			"to": "Colton Phillips <coltonjphillips@gmail.com>",
			"subject": "Hello Colton Phillips","text": "Congratulations Colton Phillips"}
		)

def define(app):
	@app.route("/test", methods = ['GET', 'POST'])
	def test():
		full_path = os.path.join(app.root_path, "static", "notes.txt")
		# append new note
		if request.method == 'POST':	
			send_simple_message()
			with Prepender(full_path) as notesFile:
				notesFile.write(request.form["note"] + "\n===\n")
	
		#get existing notes
		notes = []
		with open(full_path,'r') as notesFile:
			notes = notesFile.read().split("===")

		# just added a note
		if request.method == 'POST':	
			return render_template("test.html", notes=notes, form=request.form)
		else: 
			return render_template("test.html", notes=notes)
