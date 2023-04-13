from modules.controller.json_management_controller import *


def get_list(path):
    return read_json(get_path(path))

