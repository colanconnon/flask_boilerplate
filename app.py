
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

load_dotenv(find_dotenv())


app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()