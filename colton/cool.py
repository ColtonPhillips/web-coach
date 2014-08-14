from flask import render_template
import logging

def define(app):
	app.logger.warning("huh...")
	@app.route("/cool")
	def cool():
		import os
		log_path = os.path.join(app.root_path, "chince.txt")
		return log_path 
		app.logger.warning("GAEEE!")
	
		return render_template("cool.html")
	#	db = neato.MySQLdb_connect_secretly()
	#b	return "00"
		#"""
		#cursor = db.cursor()
		#cursor.execute("""SELECT * FROM tap""")
		#result = cursor.fetchall()
		#return str(result)
		#"""

