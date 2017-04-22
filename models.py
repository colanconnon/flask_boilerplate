from database import db
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import generate_password_hash, \
     check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password_hash = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_valid(self):
        if self.username is None or len(self.username) == 0:
            return False
        if self.password_hash is None or len(self.password_hash) == 0:
            return False
        return True
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

class Todo(db.Model):

    __tablename__ = 'todoes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name
