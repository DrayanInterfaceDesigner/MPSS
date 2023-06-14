from flask import Blueprint, render_template
from modules.controller.list_controller import *
from model import Entity


_entity = Blueprint("entities", __name__, static_folder="../static", template_folder="../view")

@_entity.route("/list", methods=["GET"])
def entity_list():
    entities = Entity.get_entities()
    return render_template("entity_list.html", entities = entities)

@_entity.route("/register", methods=["GET"])
def entity_register():
    entities = Entity.get_entities()
    return render_template("entity_register.html", entities = entities)

