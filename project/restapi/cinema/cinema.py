from flask import Blueprint
cinemas = Blueprint('cinemas', __name__, url_prefix='/v1/cinemas')


@cinemas.route('/', methods=['GET'])
def teste():
    return "aeeee"