import unittest
from app import app
from database import db
import json

class UserAuthenticationTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_it_cant_register_invalid_user(self):
        request_data = {
            "username": "test"
        }
        response = self.app.post(
            '/register',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data["error"])


    def test_it_can_register_user(self):
        request_data = {
            "username": "test",
            "password": "test"
        }
        response = self.app.post(
            '/register',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data["username"], request_data["username"])

    def test_it_cant_login_user_wrong_password(self):
        request_data = {
            "username": "test",
            "password": "test1"
        }
        response = self.app.post(
            '/login',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data["error"])


    def test_it_cant_login_user_wrong_username(self):
        request_data = {
            "username": "test1",
            "password": "test"
        }
        response = self.app.post(
            '/login',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data["error"])

    def test_it_can_login_user(self):
        request_data = {
            "username": "test",
            "password": "test"
        }
        response = self.app.post(
            '/register',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        request_data = {
            "username": "test",
            "password": "test"
        }
        response = self.app.post(
            '/login',
            data=json.dumps(request_data),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data["token"])

