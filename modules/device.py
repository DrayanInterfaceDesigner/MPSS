from flask import Blueprint, render_template, redirect, request
from modules.controller.list_controller import *
from model import Device, Sensor

_device = Blueprint("devices", __name__, static_folder="../static", template_folder="../view")

@_device.route("/list", methods=["GET"])
def device_list():
    devices = Device.get_devices()
    return render_template("device_list.html", devices = devices)

@_device.route("/register")
def device_register():
    return render_template("device_register.html")

@_device.route("/save", methods=["POST"])
def device_save():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    voltage = request.form.get("voltage")
    status_checkbox = request.form.get("status")
    status = False
    if status_checkbox == 'on':
        status = True
    measure = "0"

    Sensor.save_sensor(name, brand, model, description, voltage, status, measure)

    return redirect('/devices/list')