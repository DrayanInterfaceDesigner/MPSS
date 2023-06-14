from flask import Blueprint, render_template

_home = Blueprint("home", __name__, static_folder="../static", template_folder="../view")

@_home.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")
