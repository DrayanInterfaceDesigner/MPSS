import json
import os

def read_json(file):
    f = open(file, encoding='utf-8')
    data = json.load(f)
    return data

def get_path(path):
    absolute_path = os.path.dirname(__file__)
    relative_path = path
    full_path = os.path.join(absolute_path, relative_path)
    return full_path