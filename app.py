
from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

load_dotenv(find_dotenv())


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db needs to be setup before routes
from routes import app_routes
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run()