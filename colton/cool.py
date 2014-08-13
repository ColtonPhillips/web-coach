from flask import render_template

def define(app):
	app.logger.error("huh...")
	@app.route("/cool")
	def cool():
		asdf = neato.log_chince("asdfasdf")
		return asdf

		
		return render_template("cool.html")
	#	db = neato.MySQLdb_connect_secretly()
	#b	return "00"
		#"""
		#cursor = db.cursor()
		#cursor.execute("""SELECT * FROM tap""")
		#result = cursor.fetchall()
		#return str(result)
		#"""

