from flask import Blueprint, render_template, redirect, request
from modules.controller.list_controller import *
from flask_login import login_required, current_user
from model import Device, Sensor

_device = Blueprint("devices", __name__, static_folder="../static", template_folder="../view")

@_device.route("/list", methods=["GET"])
@login_required
def device_list():
    devices = Device.get_devices()
    return render_template("device_list.html", devices = devices)

@_device.route("/list/camera")
@login_required
def device_list_camera():
    return render_template("cameras_list.html")

@_device.route("/list/actuator")
@login_required
def device_list_actuator():
    return render_template("actuators_list.html")

@_device.route("/list/sensor")
@login_required
def device_list_sensor():
    return render_template("sensors_list.html")



@_device.route("/register")
@login_required
def device_register():
    return render_template("device_register.html")

@_device.route("/register/camera")
@login_required
def device_register_camera():
    return render_template("camera_register.html")

@_device.route("/register/actuator")
@login_required
def device_register_actuator():
    return render_template("actuator_register.html")

@_device.route("/register/sensor")
@login_required
def device_register_sensor():
    return render_template("sensor_register.html")

@_device.route("/save", methods=["POST"])
@login_required
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