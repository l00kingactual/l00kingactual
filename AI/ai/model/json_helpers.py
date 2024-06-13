# json_helpers.py
import json

def read_memory(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def update_memory(memory, filename):
    with open(filename, 'w') as f:
        json.dump(memory, f)
