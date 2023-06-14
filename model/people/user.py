from model.db import db
from model.people.person import Person
from model.people.address import Address

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), db.ForeignKey(Person.id), primary_key = True)
    license = db.Column(db.String(45))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False)
    is_Admin = db.Column(db.Boolean(), nullable=False, default=False)

    def get_users():
        users = User.query.join(Person, Person.id == User.id).join(Address, Address.person_id == User.id)\
                    .add_columns(User.id, Person.name, Person.cpf, Person.gender,
                                 Person.birth_date, Person.phone, User.license,
                                 User.email, User.username, User.password, User.is_Admin,
                                 Address.state, Address.city, Address.country, 
                                 Address.street, Address.number, Address.complement,
                                 Address.zip_code).all()
        return users
    
    def save_user(name, cpf, gender, birth_date, phone, license, username, email,
                  password, state, city, country, street, number, complement, zip_code):
        person = Person(name=name, cpf=cpf, gender=gender, birth_date=birth_date, phone=phone)
        
        user = User(id=person.id, license=license, username=username, email=email, password=password, is_Admin=False)

        address = Address(person_id=person.id, state=state, city=city, country=country, street=street,
                          number=number, complement=complement, zip_code=zip_code)

        person.users.append(user)
        person.addresses.append(address)
        db.session.add(person)
        db.session.commit()

    def delete_user(id):
        try:
            Person.query.filter_by(id=id).delete()
            User.query.filter_by(id=id).delete()
            Address.query.filter_by(person_id=id)
            db.session.commit()
            return True
        except:
            return False
        
    def update_user(data):
        Person.query.filter_by(id=data['id'])\
                .update(dict(name=data['name'], cpf=data['cpf'], gender=data['gender'], birth_date=data['birth_date'], phone=data['phone']))
        User.query.filter_by(id=data['id'])\
                .update(dict(license=data['license'], username=data['username'], email=data['email'], password=data['password'], is_Admin=data['is_Admin']))
        Address.query.filter_by(person_id=data['id'])\
                .update(dict(state=data['state'], city=data['city'], country=data['country'], 
                             street=data['street'], number=data['number'], complement=data['complement'], 
                             zip_code=data['zip_code']))
        db.session.commit()

    def make_admin(id):
        User.query.filter_by(id=id).update(dict(is_Admin=True))
        db.session.commit()