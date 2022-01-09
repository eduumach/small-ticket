from flask import Flask, jsonify
from project.ext import configuration


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)

    @app.route('/')
    def hello():
        return jsonify({'message': 'ola mundão!'})

    return app
