import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from dotenv import load_dotenv, find_dotenv
from database import db

import os
import unittest
import coverage

COV = coverage.coverage(
    branch=True,
    include='src/*',
    omit=[
        'tests/*',
        'src/__init__.py'
    ]
)
COV.start()

load_dotenv(find_dotenv())
app.config.from_object(os.environ.get('APP_SETTINGS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1

if __name__ == '__main__':
    manager.run()