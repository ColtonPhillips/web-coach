from flask import render_template

def define(app):
	@app.route("/test")
	def test():
		if request.method == 'POST':	
			return render_template("boiler.html")
		else: 
			return render_template("test.html")
		return render_template("test.html")