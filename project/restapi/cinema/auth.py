import datetime
import os
import jwt
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from functools import wraps
from .cinema import cinema_by_email

auth = Blueprint('auth_cinema', __name__, url_prefix='/v1/cinemas/auth')


@auth.route('/', methods=['POST'])
def auth_post():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    cinema = cinema_by_email(auth.username)
    if not cinema:
        return jsonify({'message': 'cinema not found', 'data': {}}), 401

    if cinema and check_password_hash(cinema.password, auth.password):
        token = jwt.encode({'username': cinema.email, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
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
            data = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=["HS256"])
            current_cinema = cinema_by_email(email=data['username'])
            if current_cinema.role == "cinema":
                return jsonify({'message': 'does not have permission to access, use a token that has the permission',
                                'data': {}}), 401
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': {}}), 401
        return f(current_cinema, *args, **kwargs)

    return decorated
