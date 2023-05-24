from flask import Flask, render_template
from modules.home import _home
from modules.register import _register
from modules.login import _login
from modules.surveillance import _surveillance
from modules.user_list import _user_list
from modules.device import _device

from model.db import db, instance


def create_app() -> Flask:
    app = Flask(__name__, template_folder="./view/",
                static_folder="./static/",
                root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    app.register_blueprint(_home)
    app.register_blueprint(_register, url_prefix="/register")
    app.register_blueprint(_login, url_prefix="/login")
    app.register_blueprint(_surveillance, url_prefix="/surveillance")
    app.register_blueprint(_user_list, url_prefix="/user_list")
    app.register_blueprint(_device, url_prefix="/devices")

    @app.route('/')
    def index():
        return render_template("home.html")

    return app