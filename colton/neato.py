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
	import os
	#my_path = os.path.join("log", "chince.txt")
	#with open(my_path,'r+') as chinceFile:
	#	chinceFile.write(str(text))
	return text	

def MySQLdb_connect_secretly():
#	log_chince("hi!")
	pass
	"""import os, MySQLdb
	my_path = os.path.join(app.root_path, "secret", "db.txt")
	with open(my_path, 'r') as secretFile:
		_host=secretFile.readline().replace("\n", "")
		_user=secretFile.readline().replace("\n", "")
		_passwd=secretFile.readline().replace("\n", "")
		_db=secretFile.readline().replace("\n", "")
		

	log_chince(_host, _user, _passwd, _db)
	return MySQLdb.connect(host=_host,user=_user,passwd=_passwd,db=_db)
	"""

from statuses import statuses
import os
from random import choice
	
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

	app.jinja_env.globals.update(get_random_status=get_random_status)
	app.jinja_env.globals.update(random_verb=random_verb)
	app.jinja_env.globals.update(random_noun=random_noun)
	app.jinja_env.globals.update(google_string=google_string)
