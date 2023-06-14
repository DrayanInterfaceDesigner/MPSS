from flask import Blueprint, render_template, redirect, request, url_for, flash
from model import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

_login = Blueprint("login", __name__, static_folder="../static", template_folder="../view/login/")

@_login.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@_login.route("/auth", methods=["GET", "POST"])
def auth():
    email = request.form.get("email")
    username = email
    password = request.form.get("password")
    remember = False
        # license = '12345678'

    user = User.query.filter_by(email=email).first()
    res = False
    if user:
        
        res = True
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect('/login') # if the user doesn't exist or password is wrong, reload the page
    else:
        # if user.isAdmin:
        #     return f"{email} : {username} : {password} : {res} : Admin? {user.isAdmin}"
        login_user(user, remember=remember)
        return redirect(url_for('home.authorized'))

# @_login.route("/in", methods=["GET", "POST"])
# def login():
#     return render_template("login.html")