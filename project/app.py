from flask import Flask, jsonify
from project.ext import configuration
from project.restapi.user.auth import token_required


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)

    @app.route('/')
    @token_required
    def hello(current_user):
        return jsonify({'message': 'ola ' + current_user.name + '!'})

    return app
