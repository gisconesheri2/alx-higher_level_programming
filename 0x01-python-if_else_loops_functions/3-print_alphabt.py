#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) == 'e' or chr(num) == 'q':
        continue
    print(chr(num), end="")
