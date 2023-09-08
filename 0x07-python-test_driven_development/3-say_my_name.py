#!/usr/bin/python3
"""joins two names to generate a full name"""


def say_my_name(first_name, last_name=""):
    """prints 'My Name is <first_name> <last_name>
    Args:
        first_name (str): first name
        last_name (str): last name - default is empty string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
