import datetime

from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Section(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    seats_id = db.Column(db.Integer, db.ForeignKey('seats.id'))
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))
    seats = db.relationship('Seats',
                            backref=db.backref('posts', lazy=True))
    cinema = db.relationship('Cinema',
                             backref=db.backref('posts', lazy=True))