from flask import render_template
import logging

def define(app):
	@app.route("/cool")
	def cool():
		log_path = os.path.join(app.root_path, "log", "chince.txt")
		return render_template("cool.html")
	#	db = neato.MySQLdb_connect_secretly()
	#b	return "00"
		#"""
		#cursor = db.cursor()
		#cursor.execute("""SELECT * FROM tap""")
		#result = cursor.fetchall()
		#return str(result)
		#"""

