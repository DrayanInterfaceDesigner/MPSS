from model.db import db

class Entity(db.Model):
    __tablename__ = "entity"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1024))
    image_url = db.Column(db.String(1024))
    first_seen = db.Column(db.DateTime)

    def get_entities():
        entities = Entity.query.all()
        return entities
    
    def save_entity(name, description, image_url, first_seen):
        entity = Entity(name=name, description=description, image_url=image_url, first_seen=first_seen)

        db.session.add(entity)
        db.session.commit()

    def delete_entity(id):
        try:
            Entity.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
        
    def update_entity(data):
        Entity.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], description=data['description'], image_url=data['image_url'], first_seen=data['first_seen']))
        db.session.commit()