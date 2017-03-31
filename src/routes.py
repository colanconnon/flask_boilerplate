from flask import Blueprint, jsonify, request
from utils import validate_json, validate_json_schema
from tasks.async.add_numbers import add_together
from flask_jwt_extended import JWTManager, jwt_required,\
    create_access_token, get_jwt_identity

app_routes = Blueprint('app_routes', __name__,
                   template_folder='templates')
from database import db
from .models import User


@app_routes.route('/', methods=['GET'])
@jwt_required
def index():
    add_together.delay(2, 2)
    return "hello world"



@app_routes.route('/register', methods=['POST'])
@validate_json
@validate_json_schema(['username', 'password'])
def register():
    user = User(username=request.json['username'], password=request.json['password'])
    if user.is_valid():
        db.session.add(user)
        db.session.commit()
        return jsonify({'username': user.username, 'id': user.id}), 201
    else:
        return jsonify({'error': "user is not valid"}), 400

@app_routes.route('/login', methods=['POST'])
@validate_json
@validate_json_schema(['username','password'])
def login():
    user = User.query.filter_by(
        username=request.json['username']).first()
    if user is None:
        return jsonify({'error': "incorrect username and password"}), 401
    if user.check_password(request.json['password']):
        return jsonify(
            {'username': user.username, 'token': create_access_token(identity=user.id)}
        ), 200
    else:
        return jsonify({'error': "incorrect username and password"}), 401
