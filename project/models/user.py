import datetime

from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    role = db.Column(db.String(50), default='user')
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password',    'role', 'created_on')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
