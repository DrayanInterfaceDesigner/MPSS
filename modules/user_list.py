from flask import Blueprint, render_template
from modules.controller.list_controller import *
from model import User

_user_list = Blueprint("user_list", __name__, static_folder="../static", template_folder="../view")

@_user_list.route("/", methods=["GET"])
def user_list():
    users = User.get_users()
    return render_template("user_list.html", users=users)

