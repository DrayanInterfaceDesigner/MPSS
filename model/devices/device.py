from model import db

class Device(db.Model):
    __tablename__ = "device"
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(30))
    model = db.Column(db.String(30))
    voltage = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(512))
    status = db.Column(db.Boolean(), nullable=False, default=False)

    sensor = db.relationship("Sensor", backref="device", lazy=True)
    camera = db.relationship("Camera", backref="device", lazy=True)