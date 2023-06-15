from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user
from modules.controller.list_controller import *
from model import Entity


_entity = Blueprint("entities", __name__, static_folder="../static", template_folder="../view")

@_entity.route("/list", methods=["GET"])
@login_required
def entity_list():
    entities = Entity.get_entities()
    return render_template("entity_list.html", entities = entities)

@_entity.route("/register", methods=["GET"])
@login_required
def entity_register():
    entities = Entity.get_entities()
    return render_template("intruder_register.html", entities = entities)

@_entity.route("/register/save", methods=["GET", "POST"])
@login_required
def entity_register_save():
    name = request.form.get("name")
    description = request.form.get("description")
    image_url = request.form.get("image_url")
    first_seen = request.form.get("first_seen")

    Entity.save_entity(name, description, image_url, first_seen)

    return redirect('/entities/list')

