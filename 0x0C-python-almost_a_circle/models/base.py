#!/usr/bin/python3
"""manages the id attribute in all classes of the package
"""
import json


class Base:
    """This class will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute
    in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the Base Class
        if id argument provided set self.id to it
        otherwise, increment the Base's __nb_objects by one
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of the JSON string representaion json_string"""
        if json_string is None or len(json_string.rstrip()) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
        to a file <Class nme>.json
        Args:
            list_objs - list of intances which inherit from Base Class
            ie Rectangle and Square instances
        """

        objs_dict_list = []
        JSON_file_name = f"{cls.__name__}.json"
        if list_objs is None or len(list_objs) == 0:
            JSON_str = "[]"
        else:
            for obj in list_objs:
                objs_dict_list.append(obj.to_dictionary())
            JSON_str = Base.to_json_string(objs_dict_list)

        with open(JSON_file_name, "w", encoding='utf-8') as fh:
            fh.write(JSON_str)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        as per values in dictionary
        """
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances of type cls"""

        JSON_file_name = f"{cls.__name__}.json"
        instances_list = []
        try:
            with open(JSON_file_name, "r", encoding='utf-8') as fh:
                JSON_str = fh.read()
                objs_list_dicts = Base.from_json_string(JSON_str)
                for obj_dict in objs_list_dicts:
                    instances_list.append(cls.create(**obj_dict))
        except FileNotFoundError:
            instances_list = []

        return (instances_list)
