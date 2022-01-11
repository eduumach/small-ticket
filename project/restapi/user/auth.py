import datetime
import os
import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash
from functools import wraps
from .users import user_by_email

auth = Blueprint('auth_user', __name__, url_prefix='/v1/users/auth')


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
                           os.environ['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing', 'data': {}}), 401
        try:
            print('aeee')
            data = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=["HS256"])
            print(data)
            current_user = user_by_email(email=data['username'])
            print(current_user)
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated
