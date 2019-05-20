import json
import os

__BASE_DIR  = os.path.dirname(os.path.dirname(__file__))

def get_settings():
    with open("{0}/{1}".format(__BASE_DIR, "../settings.json")) as datafile:
        data = json.load(datafile)
    return data
