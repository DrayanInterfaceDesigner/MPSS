from model import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

def generate_seeds(db:SQLAlchemy):
    device1 = Device(name = "dispositivo teste", brand = 'xiaomi', model = 'modelo3', voltage = '220', description = 'descricao lalalalalala', status = True)
    device2 = Device(name = "dispositivo teste 2", brand = 'apple', model = 'modelolololololo', voltage = '230', description = 'descricao lal232alalalala', status = False)
    device3 = Device(name = "dispositivo teste 3", brand = 'raspberry pi', model = 'moom', voltage = '110', description = 'descricao lalalalsdfsalala', status = True)
    
    db.session.add_all([device1, device2, device3])
    db.session.commit()

    entity1 = Entity(name = 'marcelo d2', description = 'rapper muito maluco', first_seen = datetime.today())
    entity2 = Entity(name = 'matue', description = 'tue tue e do karalyw', first_seen = datetime.today())
    entity3 = Entity(name = 'projota', description = 'rapper amorzinho videogame', first_seen = datetime.today())

    db.session.add_all([entity1, entity2, entity3])
    db.session.commit()