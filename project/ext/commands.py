from project.ext.database import db


def create_db():
    db.create_all()


def init_app(app):
    for command in [create_db]:
        app.cli.add_command(app.cli.command()(command))
