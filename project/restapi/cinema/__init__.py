from .cinema import cinemas


def init_app(app):
    app.register_blueprint(cinemas)
