from flask import Blueprint, render_template, redirect, request, url_for, flash
from model import User
from werkzeug.security import generate_password_hash, check_password_hash

_login = Blueprint("login", __name__, static_folder="../static", template_folder="../view/login/")

@_login.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@_login.route("/auth", methods=["GET", "POST"])
def auth():
    email = request.form.get("email")
    username = email
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    res = False
    if user:
        
        res = True
    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return f"YOU SHALL NOT PASS\n {email} : {username} : {password} : {res} \n {user.email}: {user.password} : {check_password_hash(user.password, password)}" # if the user doesn't exist or password is wrong, reload the page
    # license = '12345678'
    else:
        # if user.isAdmin:
        #     return f"{email} : {username} : {password} : {res} : Admin? {user.isAdmin}"
        return f"{email} : {username} : {password} : {res}"

# @_login.route("/in", methods=["GET", "POST"])
# def login():
#     return render_template("login.html")