from werkzeug.security import generate_password_hash
from flask import request, jsonify, Blueprint
from project.ext.database import db
from project.models.user import User, user_schema, users_schema

users = Blueprint('user', __name__, url_prefix='/v1/users')


@users.route('/', methods=['POST'])
def post_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    pass_hash = generate_password_hash(password)
    user = User(name, email, pass_hash)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@users.route('/<id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    user = User.query.get(id)

    if not user:
        return jsonify({'message': "user don't exist", 'date': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        user.name = name
        user.email = email
        user.password = pass_hash
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@users.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'unable to create', 'data': {}})


@users.route('/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'unable to create', 'data': {}})


def user_by_email(email):
    try:
        return User.query.filter(User.email == email).one()
    except:
        return None
