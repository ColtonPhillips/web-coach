import os 
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery
from random import choice
from statuses import statuses
app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jinja environment
app.jinja_env.globals.update(**all_definitions)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

gallery.define(app, "sketches", "/sketches", "sketches")
gallery.define(app, "my pixels", "/pixels", "pixels")

@app.route("/gear")
def gear():
	return render_template("gear.html")

@app.route("/indiewishlist")
def indiewishlist():
	return render_template("indiewishlist.html")

@app.route("/")
def main():
	return render_template("main.html")

def get_random_status():
	return choice(statuses)
app.jinja_env.globals.update(get_random_status=get_random_status)

def get_googley_div(link):
	return "- " + link + "<br>"	
app.jinja_env.globals.update(get_googley_div=get_googley_div)

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)

