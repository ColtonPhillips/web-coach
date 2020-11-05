# import urllib2, re, random
import re, random
from flask import render_template
# from bs4 import BeautifulSoup

def define(app):
	@app.route("/mario")
	def mario():
		return "TEST"
		# url = "https://supermariomakerbookmark.nintendo.net/profile/ColtonPhillips"	
		# # data = urllib2.urlopen(url).read()
		# courses = re.findall('href="/courses/(.*?)"',data, re.DOTALL)
		# soup = BeautifulSoup(data, 'html.parser')
		# names = soup.find_all("div", class_="course-title")
		# names[:] = [s.string for s in names]
		# return render_template("mario.html", levels=zip(courses, names))
