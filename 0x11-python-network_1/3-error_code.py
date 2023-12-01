#!/usr/bin/python3
"""
connect to given url and handle errors raised
"""
import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            html = resp.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
