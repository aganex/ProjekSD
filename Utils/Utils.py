import json
import os

def muat_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_json(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
