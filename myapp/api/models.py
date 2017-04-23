from .. import db
from werkzeug.security import generate_password_hash, \
     check_password_hash
import datetime
import jwt
import os

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def is_valid(self):
        if self.username is None or len(self.username) == 0:
            return False
        return True
