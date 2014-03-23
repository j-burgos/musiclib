from flask.ext.script import Manager
from models import db
from musiclib import app
from admin import admin

db.init_app(app)
admin.init_app(app)

manager = Manager(app)

@manager.command
def createdb(env="dev"):
	""" Creates the database schema """
	app.config.from_object('config.{}Config'.format(env.title()))
	db.create_all()
	
@manager.command
def runserver(env="dev"):
	""" Starts the server with the given environment """
	app.config.from_object('config.{}Config'.format(env.title()))
	app.run(app.config['LISTEN_IP'],
		port=app.config['PORT'],
		debug=app.config['DEBUG'])

if __name__ == "__main__":
	manager.run()