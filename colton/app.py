from flask import Flask, render_template
app = Flask(__name__)

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
			}
		}

@app.route("/")
def hello():
	return render_template("main.html", projects=PROJECTS, links=SIDEBAR_LINKS)

if __name__ == "__main__":
	app.run(debug=True)
