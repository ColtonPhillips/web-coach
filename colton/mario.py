

import urllib2, re, random
from flask import render_template

def define(app):
	@app.route("/mario")
	def mario():
        url = "https://supermariomakerbookmark.nintendo.net/profile/ColtonPhillips"
        data = urllib2.urlopen(url).read()
        levels = re.findall('href="/courses/(.*?)"',data , re.DOTALL)
		random.shuffle(levels)
		return render_template("mario.html", levels=levels)
