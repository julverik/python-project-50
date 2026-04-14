import json

import yaml


def parse_file(file_path):
    with open(file_path) as f:
        if file_path.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        elif file_path.endswith('.json'):
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {file_path}")