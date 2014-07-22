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

def MySQLdb_connect_secretly():
	import os, MySQLdb
	path = os.path.join(app.root_path, "secret", "db.txt")
	with open(path, 'r') as secretFile:
		_host=secretFile.readline().replace("\n", "")
		_user=secretFile.readline().replace("\n", "")
		_passwd=secretFile.readline().replace("\n", "")
		_db=secretFile.readline().replace("\n", "")

	return MySQLdb.connect(host=_host,user=_user,passwd=_passwd,db=_db)

