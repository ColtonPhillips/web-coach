import os
from flask import Flask, render_template, send_from_directory
from definitions import all_definitions

app = Flask(__name__)

# To make definitions available in the templates,
# we need to add them to the jina environment
app.jinja_env.globals.update(**all_definitions)

GALLERY_PATH = os.path.join(app.root_path, 'static', 'images', 'gallery')

@app.route('/favicon.ico')
def favicon():
	    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
			    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/gallery")
def gallery():
	pictures = []
	for image_file in os.listdir(GALLERY_PATH):
		source = "/static/images/gallery/" + image_file
		name, _ = os.path.splitext(image_file)
		pictures.append((name, source))

	return render_template("gallery.html", pictures=pictures)

@app.route("/")
def main():
	return render_template("main.html")

if __name__ == "__main__":
	# TODO: read debug setting out of a config file
	app.run(debug=True)
