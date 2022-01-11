from project.ext.database import db
from project.app import create_app

db.create_all(app=create_app())
