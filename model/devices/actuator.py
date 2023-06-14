from model.db import db
from model import Device

class Actuator(db.Model):
    __tablename__ = "actuator"
    id = db.Column(db.Integer(), db.ForeignKey(Device.id), primary_key = True)
    type = db.Column(db.String(30))

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.id)\
                    .add_columns(Actuator.id, Device.name, Device.brand, Device.model,
                                 Device.voltage, Device.description, Device.status,
                                 Actuator.type).all()
        return actuators
    
    def save_actuator(name, brand, model, description, voltage, status, type):
        device = Device(name=name, brand=brand, model=model, 
                            description=description, voltage=voltage, status=status)
        
        actuator = Actuator(id=device.id, type=type)

        device.actuators.append(actuator)
        db.session.add(device)
        db.session.commit()

    def delete_actuator(id):
        try:
            Actuator.query.filter_by(id=id).delete()
            Device.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
        
    def update_actuator(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], brand=data['brand'], model=data['model'], 
                            description=data['description'], voltage=data['voltage'], status=data['status']))
        Actuator.query.filter_by(id=data['id'])\
                .update(dict(type=data['type']))
        db.session.commit()