#!/usr/bin/python3
""" contains the base class for geometry modules """
import json
import os.path
import csv


class Base:
    """ the base geometry class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ inits class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            shape = cls(1, 1)
        elif cls.__name__ is "Square":
            shape = cls(1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for i in list_objs:
                content.append(cls.to_dictionary(i)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(content))

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"

        if not os.path.isfile(filename):
            return []
        else:
            with open(filename, "r", encoding="utf-8") as f:
                return [cls.create(**dic) for dic in
                    cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is not None:
                writer = csv.DictWriter(myFile, fieldnames=fields)
                writer.writeheader()
                for x in list_objs:
                    writer.writerow(x.to_dictionary())
            else:
                dict_writer = csv.writer(f)
                dict_writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"

        if not os.path.isfile(filename):
            return []
        else:
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                csvs = [row for row in reader]
                for row in csvs:
                    for key, value in row.items():
                        try:
                            row[key] = int(value)
                        except:
                            pass
            return [cls.create(**dic) for dic in csvs]
