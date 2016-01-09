import urllib2, re, random
from flask import render_template

def define(app):
	@app.route("/mario")
	def mario():	
		url = "https://supermariomakerbookmark.nintendo.net/profile/ColtonPhillips"	
		data = urllib2.urlopen(url).read()
		data1 = data
		courses = re.findall('href="/courses/(.*?)"',data, re.DOTALL)
		names = re.findall('class="course-title">(.*?)</div>',data1, re.DOTALL)
		#return render_template("mario.html", levels=zip(courses, names))
		return render_template("mario.html", levels=courses, names=names)
