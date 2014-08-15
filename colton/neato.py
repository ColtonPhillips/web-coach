import os
from statuses import statuses
from random import choice
from definitions import all_definitions

#http://stackoverflow.com/questions/2677617/python-f-write-at-beginning-of-file
class Prepender:
	def __init__(self, fname, mode='r+'):
		with open(fname, mode) as f:
			self.__write_queue = f.readlines()
		self.__f = open(fname, mode)

	def write(self, s):
		self.__write_queue.insert(0, s)

	def close(self):
		self.__exit__(None,None,None)

	def __enter__(self):
		return self

	def __exit__(self, type, value, trackback):
		if self.__write_queue:
			self.__f.writelines(self.__write_queue)
		self.__f.close()	

def log_chince(text):
	from app import APP_ROOT_PATH
	from datetime import datetime
	log_path = os.path.join(APP_ROOT_PATH, "log", "chince.txt") 
	with open(log_path,'a') as _f:
		now = datetime.now()
		_f.write(str(now.day) + " " + str(now.hour) + " " + str(now.minute) + "\n")
		_f.write(str(text))
		_f.write("\n\n")

def MySQLdb_connect_secretly():
	import MySQLdb
	from app import APP_ROOT_PATH
	deets_path = os.path.join(APP_ROOT_PATH, "secret", "db.txt")
	with open(deets_path, 'r') as _f:
		deets = _f.read().splitlines()
	db = MySQLdb.connect(host=deets[0],
			user=deets[1],
			passwd=deets[2],
			db=deets[3])
	return db

def define_globals(app):
	def get_random_status():
		return choice(statuses)

	def random_verb():
		full_path = os.path.join(app.root_path, "static", "verbs.txt")
		with open(full_path,'r') as verbFile:
			verbs = verbFile.read().split()
		return choice(verbs)

	def random_noun():
		full_path = os.path.join(app.root_path, "static", "nouns.txt")
		with open(full_path,'r') as nounFile:
			nouns = nounFile.read().split()
		return choice(nouns)

	def google_string(link):
		google_string = link.replace('"',"%22").replace(" ","%20")
		google_search = "https://www.google.com/search?q=" + google_string
		return google_search

	app.jinja_env.globals.update(**all_definitions)
	app.jinja_env.globals.update(get_random_status=get_random_status)
	app.jinja_env.globals.update(random_verb=random_verb)
	app.jinja_env.globals.update(random_noun=random_noun)
	app.jinja_env.globals.update(google_string=google_string)
