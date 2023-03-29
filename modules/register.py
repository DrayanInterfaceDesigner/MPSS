from flask import Blueprint, redirect, render_template

_register = Blueprint("register", __name__, static_folder="../static", template_folder="../view")

@_register.route("/", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@_register.route("/create", methods=["GET"])
def create():
    return redirect("/login")