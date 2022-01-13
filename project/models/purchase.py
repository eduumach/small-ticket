from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Purchase(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    film_name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    start_time = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.String(50), unique=True, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('relationalpurchase.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    user = db.relationship('RelationalPurchase',
                           backref=db.backref('posts', lazy=True))
    cinema = db.relationship('Section',
                             backref=db.backref('posts', lazy=True))
