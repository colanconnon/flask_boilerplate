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
        self.password_hash = self.set_password(password)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_valid(self):
        print(self.password_hash)
        if len(self.username) == 0 or self.username is None:
            return False
        if len(self.password_hash) == 0 or self.password_hash is None:
            return False
        return True
    
    def __repr__(self):
        return '<id {}>'.format(self.id)
