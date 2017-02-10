from flask import Blueprint, jsonify, request
from utils import validate_json, validate_json_schema
from tasks.async.add_numbers import add_together

app_routes = Blueprint('app_routes', __name__,
                   template_folder='templates')
from database import db
from models import User


@app_routes.route('/', methods=['GET'])
def index():
    add_together.delay(2, 2)
    return "hello world"


@app_routes.route('/register', methods=['POST'])
@validate_json
@validate_json_schema(['email', 'password'])
def register():
    if request.method == 'POST':
        user = User(username=request.json['username'], password=request.json['password'])
        if user.is_valid():
            db.session.add(user)
            db.session.commit()
            return jsonify({'username': user.username, 'success': True})
        else:
            return jsonify({'error': "user is not valid"})

@app_routes.route('/login', methods=['POST'])
@validate_json
@validate_json_schema(['username','password'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.json['username']).first()
        if user is None:
            response = jsonify({'error': "incorrect username and password"})
            response.status_code = 400
            return response
        if user.check_password(request.json['password']):
            response = jsonify({'username': user.username, 'success': True})
            response.status_code = 200
            return response
        else:
            response = jsonify({'error': "incorrect username and password"})
            response.status_code = 400
            return response
    else:
        response = jsonify({'error': "incorrect username and password"})
        response.status_code = 404
        return response
