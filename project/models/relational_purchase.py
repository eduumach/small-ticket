from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class RelationalPurchase(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('section.id'))
    user = db.relationship('User',
                           backref=db.backref('posts', lazy=True))
    cinema = db.relationship('Section',
                             backref=db.backref('posts', lazy=True))
