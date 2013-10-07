from flask import Flask, render_template
app = Flask(__name__)

SIDEBAR_LINKS = [
		("TWITTER", "https://twitter.com/ColtonPhillips"),
		("GITHUB", "https://github.com/ColtonPhillips"),
		("SOUNDCLOUD", "https://soundcloud.com/coltonphillips"),
		("YOUTUBE", "http://www.youtube.com/user/ColtonPhillips")
		]

PROJECTS = {
		"Some Game": {
			"link": "http://www.whatever.com",
			"description": "A game about a thing."
			}
		}

@app.route("/")
def hello():
	return render_template("hello.html", projects=PROJECTS, links=SIDEBAR_LINKS)

if __name__ == "__main__":
	app.run(debug=True)
