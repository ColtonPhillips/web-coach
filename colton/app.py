import os
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery

app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jina environment
app.jinja_env.globals.update(**all_definitions)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

GALLERY_PATH = os.path.join(app.root_path, 'static', 'images', 'gallery')
gallery.define(app, "Main Gallery", "/gallery", GALLERY_PATH)

ADIPOSE_SCORE_PATH = os.path.join(app.root_path, 'static','scores','adipose.score')
@app.route("/static/scores/adipose", methods=["GET", "POST"])
def get_adipose_score():
	if request.method == "POST":
		with open(ADIPOSE_SCORE_PATH) as _f:
			_f.write('b')
	else if request.method == "GET":
		with open(ADIPOSE_SCORE_PATH): as _f:
			_f.write('a')

	with open(ADIPOSE_SCORE_PATH, "r") as myfile:
		return ADIPOSE_SCORE_PATH + myfile.read()

@app.route("/")
def main():
	return render_template("main.html")

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)
