from flask import render_template, request
import requests
import os

def send_simple_message(whine):
	return requests.post(
		"https://api.mailgun.net/v2/sandboxb161ba3bb2314de2805f53614cfa0e1d.mailgun.org/messages",
		auth=("api", "key-844od-esiggre7cm8oju8walodfqkn26"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxb161ba3bb2314de2805f53614cfa0e1d.mailgun.org>",
			"to": "Colton Phillips <coltonjphillips@gmail.com>",
			"subject": "Hello Colton Phillips","text": whine}
		)

def define(app):
	@app.route("/complain", methods = ['GET', 'POST'])
	def complain():
		if request.method == 'POST':	
			send_simple_message(request.form["complaint"])
			return render_template("complain.html", form=request.form)
		else: 
			return render_template("complain.html")
