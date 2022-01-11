from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class CinemaRoom(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(512), nullable=False)

    seats_id = db.Column(db.Integer, db.ForeignKey('seats.id'))
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))
    seats = db.relationship('Seats',
                            backref=db.backref('posts', lazy=True))
    cinema = db.relationship('Cinema',
                             backref=db.backref('posts', lazy=True))
