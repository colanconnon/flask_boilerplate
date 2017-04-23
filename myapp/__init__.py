from flask import Flask
import os
from celery import Celery
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
load_dotenv(find_dotenv())

db = SQLAlchemy()


celery = Celery(__name__, backend=os.environ.get('CELERY_RESULT_BACKEND'),
                broker=os.environ.get('CELERY_BROKER_URL'))

from .async_tasks import run_flask_request
from .tasks.add_numbers import add_together

def create_app(main=True):

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_SETTINGS'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    jwt = JWTManager(app)
    db.init_app(app)

    # db needs to be setup before routes
    from .api.routes import app_routes
    from .async_tasks import tasks_bp
    app.register_blueprint(app_routes)
    app.register_blueprint(tasks_bp)
    return app