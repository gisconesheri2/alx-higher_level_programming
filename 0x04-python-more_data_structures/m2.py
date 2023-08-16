#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "I"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MLXVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCXLVI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
