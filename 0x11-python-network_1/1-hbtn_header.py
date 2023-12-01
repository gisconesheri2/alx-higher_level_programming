#!/usr/bin/python3
"""
connect to given url and print the value of the X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        html = resp.read()
        headers = resp.info()
        print(headers.get('X-Request-Id'))
