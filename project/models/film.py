from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class CinemaRoom(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(512), nullable=False)
    duration = db.Colmun(db.Integer, nullable=False)
