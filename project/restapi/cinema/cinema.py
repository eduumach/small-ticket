from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from project.ext.database import db
from project.models.cinema import Cinema, cinema_schema, cinemas_schema

cinemas = Blueprint('cinemas', __name__, url_prefix='/v1/cinemas')


@cinemas.route('/', methods=['POST'])
def post_user():
    name = request.json['name']
    email = request.json['email']
    cnpj = request.json['cnpj']
    password = request.json['password']
    pass_hash = generate_password_hash(password)
    cinema = Cinema(name, email, cnpj, pass_hash)

    try:
        db.session.add(cinema)
        db.session.commit()
        result = cinema_schema.dump(cinema)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@cinemas.route('/<id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    cnpj = request.json['cnpj']
    password = request.json['password']

    cinema = Cinema.query.get(id)

    if not cinema:
        return jsonify({'message': "cinema don't exist", 'date': {}}), 404

    pass_hash = generate_password_hash(password)

    try:
        cinema.name = name
        cinema.email = email
        cinema.cnpj = cnpj
        cinema.password = pass_hash
        db.session.add(cinema)
        db.session.commit()
        result = cinema_schema.dump(cinema)
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500


@cinemas.route('/', methods=['GET'])
def get_users():
    users = Cinema.query.all()
    if users:
        result = cinemas_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'unable to create', 'data': {}})


@cinemas.route('/<id>', methods=['GET'])
def get_user(id):
    cinemas = Cinema.query.get(id)
    if cinemas:
        result = cinemas_schema.dump(cinemas)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'unable to create', 'data': {}})


def cinema_by_email(email):
    try:
        return Cinema.query.filter(Cinema.email == email).one()
    except:
        return None
