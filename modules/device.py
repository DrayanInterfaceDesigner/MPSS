from flask import Blueprint, render_template, redirect, request
from modules.controller.list_controller import *
from flask_login import login_required, current_user
from model import Device, Sensor, Camera, Actuator

_device = Blueprint("devices", __name__, static_folder="../static", template_folder="../view")

@_device.route("/list", methods=["GET"])
@login_required
def device_list():
    return render_template("device_list.html")

@_device.route("/list/camera")
@login_required
def device_list_camera():
    devices = Camera.get_cameras()
    return render_template("cameras_list.html", devices = devices)

@_device.route("/list/actuator")
@login_required
def device_list_actuator():
    devices = Actuator.get_actuators()
    return render_template("actuators_list.html", devices = devices)

@_device.route("/list/sensor")
@login_required
def device_list_sensor():
    devices = Sensor.get_sensors()
    return render_template("sensors_list.html", devices = devices)



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

@_device.route("/register/camera/save", methods=["POST"])
@login_required
def camera_save():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    voltage = request.form.get("voltage")
    status_checkbox = request.form.get("status")
    resolution = request.form.get("resolution")
    status = False
    if status_checkbox == 'on':
        status = True

    Camera.save_camera(name, brand, model, description, voltage, status, resolution)

    return redirect('/devices/list/camera')

@_device.route("/register/sensor/save", methods=["POST"])
@login_required
def sensor_save():
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

    return redirect('/devices/list/sensor')

@_device.route("/register/actuator/save", methods=["POST"])
@login_required
def actuator_save():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    voltage = request.form.get("voltage")
    status_checkbox = request.form.get("status")
    _type = request.form.get("type")
    if status_checkbox == 'on':
        status = True

    Sensor.save_sensor(name, brand, model, description, voltage, status, _type)

    return redirect('/devices/list/actuator')

