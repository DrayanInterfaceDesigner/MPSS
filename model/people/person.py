from model.db import db

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(11), unique=True)
    gender = db.Column(db.String(1))
    birth_date  = db.Column(db.DateTime)
    phone = db.Column(db.String(15))

    users = db.relationship('User', backref='person')
    addresses = db.relationship('Address', backref='person')