from .users import users
from .auth import auth


def init_app(app):
    app.register_blueprint(users)
    app.register_blueprint(auth)
