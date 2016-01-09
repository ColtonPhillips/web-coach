import urllib2, re, random
from flask import render_template
from bs4 import BeautifulSoup

def define(app):
	@app.route("/mario")
	def mario():	
		url = "https://supermariomakerbookmark.nintendo.net/profile/ColtonPhillips"	
		data = urllib2.urlopen(url).read()
		courses = re.findall('href="/courses/(.*?)"',data, re.DOTALL)
		#names = re.findall('<div class="course-title">(.*?)</div>',data1, re.DOTALL)	
		soup = BeautifulSoup(data, 'html.parser')
		#names = soup.find_all('course-title')
		names = ["1","a"]
		#return render_template("mario.html", levels=zip(courses, names))
		return render_template("mario.html", levels=courses, names=names)
