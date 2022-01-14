from .cinema import cinemas
from .auth import auth


def init_app(app):
    app.register_blueprint(cinemas)
    app.register_blueprint(auth)
