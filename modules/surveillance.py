from flask import Blueprint, render_template, request, jsonify, Response
from flask_login import login_required
from model.mqtt import mqtt_client, topic_send
import time

_surveillance = Blueprint("surveillance", __name__, static_folder="../static", template_folder="../view")

devices = [["detector_de_presença", "sinal"]]

@_surveillance.route("/", methods=["GET", "POST"])
@login_required
def surveillance():
    return render_template("surveillance.html", devices=devices)

@_surveillance.route('/stream')
@login_required
def stream():
    def generate_events():
        for i in range(1, 6):
            yield f'data: Message {i}\n\n'
            time.sleep(1)
    return Response(generate_events(), mimetype='text/event-stream')

@_surveillance.route("/emergency", methods=["GET", "POST"])
@login_required
def emergency():
    message = "Fudeu!!!!!"
    publish_result = mqtt_client.publish(topic_send, message)
    print("Atuador acionado!")
    return jsonify(publish_result)
