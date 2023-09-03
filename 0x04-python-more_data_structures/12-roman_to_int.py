#!/usr/bin/python3


def roman_to_int(roman_string):

    roman_num = dict(V=5, X=10, L=50, C=100, D=500, M=1000)
    roman_num["I"] = 1
    dec = 0
    last_letter = ""

    if type(roman_string) != str or roman_string is None:
        return 0

    if len(roman_string) == 1:
        return (roman_num[roman_string])

    for let in roman_string:
        if last_letter == "I" and let == "X":
            dec += 8
            continue
        if last_letter == "I" and let == "V":
            dec += 3
            continue
        if last_letter == "X" and let == "L":
            dec += 30
            continue
        if last_letter == "X" and let == "C":
            dec += 80
            continue
        if last_letter == "C" and let == "D":
            dec += 390
            continue
        if last_letter == "C" and let == "M":
            dec += 890
            continue
        dec += roman_num[let]
        last_letter = let

    return (dec)
