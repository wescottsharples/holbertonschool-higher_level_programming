#!/usr/bin/python3
""" Function returns object loaded from JSON string """


def from_json_string(my_str):
    import json
    return json.loads(my_str)
