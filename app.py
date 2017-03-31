
from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager

load_dotenv(find_dotenv())


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)

# db needs to be setup before routes
from src.routes import app_routes
app.register_blueprint(app_routes)



if __name__ == '__main__':
    app.run()