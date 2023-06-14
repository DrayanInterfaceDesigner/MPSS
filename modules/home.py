from flask import Blueprint, render_template
from flask_login import login_required, current_user

_home = Blueprint("home", __name__, static_folder="../static", template_folder="../view")

@_home.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@_home.route("/authorized", methods=["GET", "POST"])
@login_required
def authorized():
    return render_template("home_authorized.html", name=current_user.username)