from flask import Blueprint, render_template
from modules.controller.user_list_controller import *


_user_list = Blueprint("user_list", __name__, static_folder="../static", template_folder="../view")
data = get_user_list("../../model/users.json")
users = []
for user in data['users']:
    users.append(user['username'])

@_user_list.route("/", methods=["GET"])
def user_list():
    return render_template("user_list.html", users=users)
