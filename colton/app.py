from flask import Flask, render_template, send_from_directory, request,url_for, redirect
from definitions import all_definitions
import os, gallery, todo, complain, neato, comic, logo, cool
from random import choice
from statuses import statuses
import MySQLdb
app = Flask(__name__)

# DEFINITIONS
# To make definitions available in the templates,
# we need to add them to the jinja environment
app.jinja_env.globals.update(**all_definitions)
neato.define_globals(app)

gallery.define(app, "sketches", "/sketches", "sketches")
gallery.define(app, "my pixels", "/pixels", "pixels")

# Each day is something new
todo.define(app)

#Phil Fish 2 Simulator
complain.define(app)

# Comic
comic.define(app)

# I am a designer
logo.define(app)

# Who is cooler?
cool.define(app)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

# This is my boilerplate code I will start with
@app.route("/boiler")
def boiler():
	return render_template("boiler.html")

# Now a word from our sponsors
@app.route("/friends")
def friends():
	return render_template("friends.html")

@app.route("/resume")
@app.route("/resume/")
def resume():
	return redirect(url_for('static', filename='resume.pdf'))

@app.route("/gear")
def gear():
	return render_template("gear.html")

@app.route("/indiewishlist")
def indiewishlist():
	return render_template("indiewishlist.html")

@app.route("/verbthenoun")
def verbthenoun():
	return render_template("verbthenoun.html")

@app.route("/")
def main():
	return render_template("main.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("pagenotfound.html"), 404

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	# TODO: Get logging to work
	app.run(debug=True)

