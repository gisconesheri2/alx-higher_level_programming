#!/usr/bin/python3
import hidden_4 as h4

if __name__ == "__main__":
    for name in dir(h4):
        if name[0] == "_":
            continue
        print(name)
