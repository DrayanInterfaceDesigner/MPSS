from model import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

def generate_seeds(db:SQLAlchemy):
    user1 = User.save_user(name = "Lucca Costa", cpf = "999999", gender = "M", birth_date = datetime.strptime("2002-07-22", "%Y-%m-%d"), phone = "41999999999", 
                 license = "license", username = "luccagamer", email = "lucca@mpss.com", password = generate_password_hash("sexo123"), state = "PR", 
                 city = "Curitiba", country = "Brazil", street = "Rua dos memes", number = "69", complement = "ap.420", zip_code = "80123123")
    user2 = User.save_user(name = "Drayan Magalhães", cpf = "999998", gender = "M", birth_date = datetime.strptime("2002-01-01", "%Y-%m-%d"), phone = "41999999999", 
                 license = "license", username = "rafaelbaguncas", email = "drayan@mpss.com", password = generate_password_hash("sexo123"), state = "PR", 
                 city = "Curitiba", country = "Brazil", street = "Rua dos memes", number = "69", complement = "ap.420", zip_code = "80123123")
    
    # db.session.add_all([user1, user2])
    # db.session.commit()

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