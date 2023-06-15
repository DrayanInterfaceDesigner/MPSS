from flask import Flask, render_template
from modules.home import _home
from modules.register import _register
from modules.login import _login
from modules.surveillance import _surveillance
from modules.user_list import _user_list
from modules.device import _device
from modules.intruder import _entity
from flask_login import LoginManager
from flask_mqtt import Mqtt
from model.mqtt import mqtt_client, topic_subscribe
from model.db import db, instance
from model import User, Read
from datetime import datetime
import time


def create_app() -> Flask:
    app = Flask(__name__, template_folder="./view/",
                static_folder="./static/",
                root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    app.config['MQTT_BROKER_URL'] = 'broker.hivemq.com'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  
    app.config['MQTT_PASSWORD'] = ''  
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

    login_manager = LoginManager()
    login_manager.login_view = 'login.auth'

    mqtt_client.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(_home)
    app.register_blueprint(_register, url_prefix="/register")
    app.register_blueprint(_login, url_prefix="/login")
    app.register_blueprint(_surveillance, url_prefix="/surveillance")
    app.register_blueprint(_user_list, url_prefix="/user_list")
    app.register_blueprint(_device, url_prefix="/devices")
    app.register_blueprint(_entity, url_prefix="/entities")

    @app.route('/')
    def index():
        return render_template("home.html")
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected succesfully!')
            for topic in topic_subscribe:
                mqtt_client.subscribe(topic, qos=0)
                print(topic)
        else:
            print("Bad connection. Code: ", rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            now=datetime.now(),
            topic=message.topic,
            payload=message.payload.decode()
        )
        with app.app_context():
            presence = Read(date_time=datetime.now(), message=message.payload.decode())
            db.session.add(presence)
            db.session.commit()

        print('Received message at {now} on topic: {topic} with payload: {payload}'.format(**data))

    return app