from model.db import db
from model import Device

class Camera(db.Model):
    __tablename__ = "camera"
    id = db.Column(db.Integer(), db.ForeignKey(Device.id), primary_key = True)
    resolution = db.Column(db.String(20))

    def get_cameras():
        cameras = Camera.query.join(Device, Device.id == Camera.id)\
                    .add_columns(Camera.id, Device.name, Device.brand, Device.model,
                                 Device.voltage, Device.description, Device.status,
                                 Camera.resolution).all()
        return cameras
    
    def save_camera(name, brand, model, description, voltage, status, resolution):
        device = Device(name=name, brand=brand, model=model, 
                            description=description, voltage=voltage, status=status)
        
        camera = Camera(id=device.id, resolution=resolution)

        device.cameras.append(camera)
        db.session.add(device)
        db.session.commit()

    def delete_camera(id):
        try:
            Camera.query.filter_by(id=id).delete()
            Device.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
        
    def update_camera(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], brand=data['brand'], model=data['model'], 
                            description=data['description'], voltage=data['voltage'], status=data['status']))
        Camera.query.filter_by(id=data['id'])\
                .update(dict(resolution=data['resolution']))
        db.session.commit()