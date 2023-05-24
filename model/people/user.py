from model.db import db
from model import Person

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), db.ForeignKey(Person.id), primary_key = True)
    license = db.Column(db.String(45))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)