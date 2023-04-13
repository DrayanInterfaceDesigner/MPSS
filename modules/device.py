from flask import Blueprint, render_template
from modules.controller.list_controller import *


_device = Blueprint("device", __name__, static_folder="../static", template_folder="../view")
data = get_list("../../model/devices.json")
devices = []
for device in data['devices']:
    devices.append({"id": device["id"], "name": device["device name"]})

@_device.route("/list", methods=["GET"])
def device_list():
    return render_template("device_list.html", devices=devices)

@_device.route("/register", methods=["GET", "POST"])
def device_register():
    return render_template("device_register.html")