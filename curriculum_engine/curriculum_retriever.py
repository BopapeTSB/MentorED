import json

CAPS_PATH = "config/caps_subject_map.json"

def retrieve_curriculum(subject):

    with open(CAPS_PATH, "r") as f:

        data = json.load(f)

    return data.get(subject, {})

