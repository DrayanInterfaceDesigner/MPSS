from model.db import db
from model import Device

class Sensor(db.Model):
    __tablename__ = "sensor"
    id = db.Column(db.Integer(), db.ForeignKey(Device.id), primary_key = True)
    measure = db.Column(db.String(20))