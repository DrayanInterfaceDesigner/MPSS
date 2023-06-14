from flask import Blueprint, render_template
from flask_login import login_required, current_user

_surveillance = Blueprint("surveillance", __name__, static_folder="../static", template_folder="../view")

devices = [["detector_de_presença", "sinal"]]

@_surveillance.route("/", methods=["GET", "POST"])
@login_required
def surveillance():
    return render_template("surveillance.html", devices=devices)

@_surveillance.route("/emergency", methods=["GET", "POST"])
@login_required
def emergency():
    return render_template("emergency.html")