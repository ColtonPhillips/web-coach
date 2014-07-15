from flask import render_template, request

def define(app):
	@app.route("/test", methods = ['GET', 'POST'])
	def test():
		if request.method == 'POST':	
			return render_template("test.html", bbb="master")#request.data)
		else: 
			return render_template("test.html")
