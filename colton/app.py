import os
from flask import Flask, render_template
from content.links import SIDEBAR_LINKS
from content.projects import PROJECTS
app = Flask(__name__)

GALLERY_PATH = str(app.root_path) + "/static/images/gallery"

@app.route("/gallery")
def gallery():
	pictures = ["/static/images/gallery/" + picture for picture in os.listdir(GALLERY_PATH)]
	return render_template("gallery.html", pictures=pictures)

@app.route("/")
def main():
	return render_template("main.html", projects=PROJECTS, links=SIDEBAR_LINKS)

if __name__ == "__main__":
	app.run(debug=True)
