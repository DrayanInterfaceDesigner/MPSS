from flask import Blueprint, render_template

_login = Blueprint("login", __name__, static_folder="../static", template_folder="../view/login/")

@_login.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")