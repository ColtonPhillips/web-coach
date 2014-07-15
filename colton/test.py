from flask import render_template

def define(app):
	@app.route("/test")
	def test():
		return render_template("test.html")

	#app.add_url_rule(route, gallery_name, gallery)
