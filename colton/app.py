import os
from flask import Flask, render_template
app = Flask(__name__)

GALLERY_PATH = str(app.root_path) + "/static/images/gallery"

SIDEBAR_LINKS = [
		("TWITTER", "https://twitter.com/ColtonPhillips"),
		("GITHUB", "https://github.com/ColtonPhillips"),
		("SOUNDCLOUD", "https://soundcloud.com/coltonphillips"),
		("YOUTUBE", "http://www.youtube.com/user/ColtonPhillips")
		]

PROJECTS = {
		"NEPTUNE: Ocean Explorer": {
			"link": "http://wordsinthesky.com/projects/neptune-ocean-explorer",
			"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget augue in purus feugiat sollicitudin ac laoreet nunc.",
			"header": "/static/images/neptune-header.png",
			"thumbnail": "/static/images/neptune-thumb.gif"
			},

		"NEPTUNE: Ocean Explorer 2": {
			"link": "http://wordsinthesky.com/projects/neptune-ocean-explorer",
			"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget augue in purus feugiat sollicitudin ac laoreet nunc.",
			"header": "/static/images/neptune-header.png",
			"thumbnail": "/static/images/neptune-thumb.gif"
			},

		"NEPTUNE: Ocean Explorer 3": {
			"link": "http://wordsinthesky.com/projects/neptune-ocean-explorer",
			"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget augue in purus feugiat sollicitudin ac laoreet nunc.",
			"header": "/static/images/neptune-header.png",
			"thumbnail": "/static/images/neptune-thumb.gif"
			},

		"NEPTUNE: Ocean Explorer 4": {
			"link": "http://wordsinthesky.com/projects/neptune-ocean-explorer",
			"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget augue in purus feugiat sollicitudin ac laoreet nunc.",
			"header": "/static/images/neptune-header.png",
			"thumbnail": "/static/images/neptune-thumb.gif"
			}
		}

@app.route("/gallery")
def gallery():
	pictures = ["/static/images/gallery/" + picture for picture in os.listdir(GALLERY_PATH)]
	return render_template("gallery.html", pictures=pictures)

@app.route("/")
def main():
	return render_template("main.html", projects=PROJECTS, links=SIDEBAR_LINKS)

if __name__ == "__main__":
	app.run(debug=True)
