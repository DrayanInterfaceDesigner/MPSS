from model.db import db
from model import Device

class Sensor(db.Model):
    __tablename__ = "sensor"
    id = db.Column(db.Integer(), db.ForeignKey(Device.id), primary_key = True)
    measure = db.Column(db.String(20))

    def get_sensors():
        sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Sensor.id, Device.name, Device.brand, Device.model,
                                 Device.voltage, Device.description, Device.status,
                                 Sensor.measure).all()
        return sensors
    
    def save_sensor(name, brand, model, description, voltage, status, measure):
        device = Device(name=name, brand=brand, model=model, 
                            description=description, voltage=voltage, status=status)
        
        sensor = Sensor(id=device.id, measure=measure)

        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()

    def delete_sensor(id):
        try:
            Sensor.query.filter_by(id=id).delete()
            Device.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
        
    def update_sensor(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], brand=data['brand'], model=data['model'], 
                            description=data['description'], voltage=data['voltage'], status=data['status']))
        Sensor.query.filter_by(id=data['id'])\
                .update(dict(measure=data['measure']))
        db.session.commit()