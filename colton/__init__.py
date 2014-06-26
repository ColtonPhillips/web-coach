from app import app

def get_random_status():
#	with open('/static/statuses.txt', 'r') as statusFile:
#		statuses = statusFile.read().split()
#	from random import choice
#	return str(choice(statuses))
	return "Hello Workd!"

app.jinja_env.globals.update(get_random_status=get_random_status)
