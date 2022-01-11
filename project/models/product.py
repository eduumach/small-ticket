from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    value = db.Column(db.Float, nullable=False)

    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))
    cinema = db.relationship('Cinema',
                             backref=db.backref('posts', lazy=True))
