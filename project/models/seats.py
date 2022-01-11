from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Seats(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    line = db.Column(db.Integer, nullable=False)
    column = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
