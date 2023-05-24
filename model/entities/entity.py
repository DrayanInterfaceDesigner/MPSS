from model.db import db

class Entity(db.Model):
    __tablename__ = "entity"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1024))
    image_url = db.Column(db.String(1024))
    first_seen = db.Column(db.DateTime)