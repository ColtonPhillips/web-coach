from flask import Flask, render_template
app = Flask(__name__)

PROJECTS = {
		"Corvus": {
			"link": "www.google.com"
			}
		}

@app.route("/")
def hello():
	return render_template("hello.html", projects=PROJECTS)

if __name__ == "__main__":
	app.run(debug=True)
