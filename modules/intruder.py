from flask import Blueprint, render_template
from modules.controller.list_controller import *


_entity = Blueprint("entities", __name__, static_folder="../static", template_folder="../view")
data = get_list("../../model/devices.json")
devices = []
for device in data['devices']:
    devices.append({"id": device["id"], "name": device["name"]})

@_entity.route("/list", methods=["GET"])
def _entity_list():
    return render_template("entity_list.html", devices=devices)
