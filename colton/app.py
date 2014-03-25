import os 
from flask import Flask, render_template, send_from_directory, request
from definitions import all_definitions
import gallery

app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jinja environment
app.jinja_env.globals.update(**all_definitions)

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

GALLERY_PATH = os.path.join(app.root_path, 'static', 'images', 'gallery')
gallery.define(app, "Main Gallery", "/gallery", GALLERY_PATH)

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

ADIPOSE_SCORE_PATH = os.path.join(app.root_path, 'static','scores','adipose.score')
@app.route("/static/scores/adipose_check_is_highest_score", methods=["GET", "POST"])
def adipose_check_is_highest_score():
	if request.method == "POST":
		with open(ADIPOSE_SCORE_PATH,'r') as _f:
			high_score = _f.readline()#name
			high_score = int(_f.readline().strip('\n'))
		score = int(request.form['score'])	
		if is_number(score):
			if score > high_score:
				return 'true'
		return 'false'
		
	elif request.method == "GET":
		return 'false'	

#TODO what if for all functions, what if the highscore is empty first. bug
@app.route("/static/scores/adipose_get_highest_score", methods=["GET", "POST"])
def adipose_get_highest_score():
	if request.method == "GET" or request.method == "POST":
		with open(ADIPOSE_SCORE_PATH,'r') as _f:
			high_score = _f.readline()#name
			high_score = int(_f.readline().strip('\n'))
			return high_score
	return "fail"
		
@app.route("/static/scores/adipose_suggest_high_score", methods=["GET", "POST"])
def adipose_suggest_high_score():
	if request.method == "POST":
		with open(ADIPOSE_SCORE_PATH,'r') as _f:
			high_score = _f.readline()#name
			high_score = int(_f.readline().strip('\n'))
		score = int(request.form['score'])	
		if is_number(score):
			if score > high_score:
				with open(ADIPOSE_SCORE_PATH, "r+") as _f:
					lines = _f.readlines()
					_f.seek(0)
					_f.write(request.form["team"]+ os.linesep)
					_f.write(request.form["score"]+ os.linesep)
					_f.writelines(lines)
				return "success"

		return 'fail'
		
	elif request.method == "GET":
		return 'fail'	

@app.route("/")
def main():
	return render_template("main.html")

#SHIT_LOG_PATH = os.path.join(app.root_path, 'shit.log')
if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)
#	import logging
#	file_handler = logging.FileHandler(SHIT_LOG_PATH) 
#	file_handler.setLevel(logging.WARNING)
#	app.logger.addHandler(file_handler)

