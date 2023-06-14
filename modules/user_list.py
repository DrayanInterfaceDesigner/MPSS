from flask import Blueprint, render_template
from modules.controller.list_controller import *
from model import User
from model import Entity


_user_list = Blueprint("user_list", __name__, static_folder="../static", template_folder="../view")

@_user_list.route("/", methods=["GET"])
def user_list():
    print("---------------------------------")
    print(Entity.get_entities())
    print("---------------------------------")
    users = User.get_users()
    print(users)
    return render_template("user_list.html", users=users)

