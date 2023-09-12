#!/usr/bin/python3
"""student class to define a student
"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve a dictionary representation of an instance
        if attrs is a list of strings, retrieve only the attribute
        names in this list, otherwise return all attributes
        """
        instance_dict = vars(self)
        class_attrs = vars(self.__class__)
        new_instance_dict = {}
        for k, v in class_attrs.items():
            if k[0:2] == "__":
                continue
            if type(v) is int or type(v) is str or type(v) is dict:
                instance_dict[k] = v
            if type(v) is bool or type(v) is list:
                instance_dict[k] = v

        if attrs is None:
            return instance_dict
        for name in attrs:
            if name in instance_dict:
                new_instance_dict[name] = instance_dict[name]
        return new_instance_dict

    def reload_from_json(self, json):
        """resets all atributes of the instance using values from json
        """
        for name, value in json.items():
            setattr(self, name, value)
