#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == "__main__":
    argl = sys.argv
    num = 1
    arg_length = len(argl)

    if (arg_length != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argl[1])
    b = int(argl[3])

    if (argl[2] == "+"):
        print("{} + {} = {}".format(a, b, calc.add(a, b)))

    elif (argl[2] == "-"):
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))

    elif (argl[2] == "*"):
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))

    elif (argl[2] == "/"):
        print("{} + {} = {}".format(a, b, calc.div(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sys.exit(0)
