import unittest
from myapp.wsgi import app
from myapp import db
import json
from src.models import User

class UserTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_valid_user(self):
        user = User("test", "test")
        self.assertTrue(user.is_valid())

    def test_invalid_user_username(self):
        user = User(None, "test")
        self.assertFalse(user.is_valid())
