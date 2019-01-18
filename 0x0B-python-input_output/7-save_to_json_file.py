#!/usr/bin/python3
""" Contains function that writes an object using JSON repr """


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
