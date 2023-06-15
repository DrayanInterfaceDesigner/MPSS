from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from model.mqtt import mqtt_client, topic_send

_surveillance = Blueprint("surveillance", __name__, static_folder="../static", template_folder="../view")

devices = [["detector_de_presença", "sinal"]]

@_surveillance.route("/", methods=["GET", "POST"])
@login_required
def surveillance():
    return render_template("surveillance.html", devices=devices)

@_surveillance.route("/emergency", methods=["GET", "POST"])
@login_required
def emergency():
    message = "Fudeu!!!!!"
    # publish_result = mqtt_client.publish(topic_send, message)
    # print(publish_result)
    return jsonify({"penis": "marcelo"})
