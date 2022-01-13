import datetime

from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Section(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_time = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullabe=False)

    seats_id = db.Column(db.Integer, db.ForeignKey('cinemaroom.id'))
    cinema_id = db.Column(db.Integer, db.ForeignKey('film.id'))
    seats = db.relationship('CinemaRoom',
                            backref=db.backref('posts', lazy=True))
    cinema = db.relationship('Film',
                             backref=db.backref('posts', lazy=True))
