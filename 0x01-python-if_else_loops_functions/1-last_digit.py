#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ln = (number * -1) % 10
    print(f"Last digit of {number} is -{ln} and is less than 6 and not 0")
else:
    ln = (number) % 10
    if ln > 5:
        print(f"Last digit of {number} is {ln} and is greater than 5")
    elif ln == 0:
        print(f"Last digit of {number} is {ln} and is 0")
    else:
        print(f"Last digit of {number} is {ln} and is less than 6 and not 0")
