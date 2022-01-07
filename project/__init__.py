from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from project.user.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from project.user.auth import auth as auth_user_blueprint
    app.register_blueprint(auth_user_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .admin.auth import auth as auth_admin_blueprint
    app.register_blueprint(auth_admin_blueprint)

    return app
