import json


def json_formatter(diff):
    return json.dumps(diff, indent=2, sort_keys=True)