from flask import Blueprint, render_template, redirect, url_for
from modules.controller.list_controller import *
from flask_login import login_required, current_user
from model import User

_user_list = Blueprint("user_list", __name__, static_folder="../static", template_folder="../view")

@_user_list.route("/", methods=["GET"])
@login_required
def user_list():
    # if(current_user.isAdmin != None):
    #     users = User.get_users()
    #     return render_template("user_list.html", users=users)
    # else:
        return redirect(url_for("home.authorized"))

