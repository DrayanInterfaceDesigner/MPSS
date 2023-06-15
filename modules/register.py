from flask import Blueprint, redirect, render_template, request, url_for
from model import User
from werkzeug.security import generate_password_hash
import datetime

_register = Blueprint("register", __name__, static_folder="../static", template_folder="../view")

@_register.route("/", methods=["GET", "POST"])
def register():
    return render_template("/login/register.html")

@_register.route("/save", methods = ["POST"])
def save():
    name = request.form.get("name")
    email = request.form.get("email")
    username = email
    cpf = request.form.get("cpf")
    gender = request.form.get("gender")
    birth_date = request.form.get("birthday")
    phone = request.form.get("phone")
    country = request.form.get("country")
    state = request.form.get("state")
    city = request.form.get("city")
    street = request.form.get("street")
    number = request.form.get("number")
    zip_code = request.form.get("zip_code")
    complement = request.form.get("complement")
    password = request.form.get("password")

    password = generate_password_hash(password)

    license = '12345678'

    User.save_user(name, cpf, gender, birth_date, phone, license, username, email,
                  password, state, city, country, street, number, complement, zip_code)

    return redirect("/login")