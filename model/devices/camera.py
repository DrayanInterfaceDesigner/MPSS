from model.db import db
from model import Device

class Camera(db.Model):
    __tablename__ = "camera"
    id = db.Column(db.Integer(), db.ForeignKey(Device.id), primary_key = True)
    resolution = db.Column(db.String(20))