from flask import Flask, render_template
from modules.home import _home
from modules.register import _register
from modules.login import _login
from modules.surveillance import _surveillance
from modules.user_list import _user_list
from modules.device import _device
from modules.intruder import _entity
from flask_login import LoginManager

from model.db import db, instance


def create_app() -> Flask:
    app = Flask(__name__, template_folder="./view/",
                static_folder="./static/",
                root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.auth'
    login_manager.init_app(app)

    from model import User
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

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

    return app