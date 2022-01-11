import datetime

from project.ext.database import db, ma
from sqlalchemy_serializer import SerializerMixin


class Cinema(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    cnpj = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    role = db.Column(db.String(50), default='cinema')
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())


    def __init__(self, name_cinema, email, cnpj, password):
        self.name_cinema = name_cinema
        self.email = email
        self.cnpj = cnpj
        self.password = password


class CinemaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'cnpj', 'password', 'role', 'created_on')


cinema_schema = CinemaSchema()
cinemas_schema = CinemaSchema(many=True)
