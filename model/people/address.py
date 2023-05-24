from model.db import db
from model import Person

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer(), primary_key=True)
    person_id = db.Column(db.Integer(), db.ForeignKey(Person.id))
    state = db.Column(db.String(2))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    street = db.Column(db.String(200))
    number = db.Column(db.String(100))
    complement = db.Column(db.String(100))
    zip_code = db.Column(db.String(15))