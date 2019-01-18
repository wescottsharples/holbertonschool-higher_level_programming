#!/usr/bin/python3
""" Contains function that creates an object from JSON file """


def load_from_json_file(filename):
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
