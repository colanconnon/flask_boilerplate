import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from database import db
from app import app
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
app.config.from_object(os.environ.get('APP_SETTINGS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()