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
	log_path = os.path.join(APP_ROOT_PATH, "log", "chince.txt") 
	with open(log_path,'r+') as _f:
		_f.write(str(text))

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
