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

    def to_json(self):
        """retrieve a dictionary representation of an instance"""
        instance_dict = vars(self)
        class_attrs = vars(self.__class__)
        for k, v in class_attrs.items():
            if k[0:2] == "__":
                continue
            if type(v) is int or type(v) is str or type(v) is dict:
                instance_dict[k] = v
            if type(v) is bool or type(v) is list:
                instance_dict[k] = v
        return instance_dict
