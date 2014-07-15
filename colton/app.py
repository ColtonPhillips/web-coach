import os 
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery
from random import choice
from statuses import statuses
import test
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

test.define(app)

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

def get_random_status():
	return choice(statuses)
app.jinja_env.globals.update(get_random_status=get_random_status)

def random_verb():
	full_path = os.path.join(app.root_path, "static", "verbs.txt")
	with open(full_path,'r') as verbFile:
		verbs = verbFile.read().split()
	return choice(verbs)
app.jinja_env.globals.update(random_verb=random_verb)

def random_noun():
	full_path = os.path.join(app.root_path, "static", "nouns.txt")
	with open(full_path,'r') as nounFile:
		nouns = nounFile.read().split()
	return choice(nouns)
app.jinja_env.globals.update(random_noun=random_noun)



def google_string(link):
	google_string = link.replace('"',"%22").replace(" ","%20")
	google_search = "https://www.google.com/search?q=" + google_string
	return google_search
app.jinja_env.globals.update(google_string=google_string)

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)

