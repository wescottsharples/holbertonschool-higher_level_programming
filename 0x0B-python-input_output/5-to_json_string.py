#!/usr/bin/python3
""" Contains function that returns JSON repr of string """


def to_json_string(my_obj):
    import json
    return json.dumps(my_obj)
