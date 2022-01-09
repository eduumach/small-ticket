import datetime

import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
from functools import wraps
from .users import user_by_email

auth = Blueprint('auth_user', __name__, url_prefix='/users/auth')


@auth.route('/', methods=['POST'])
def auth_post():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    user = user_by_email(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           current_app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
