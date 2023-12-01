#!/usr/bin/python3
"""
connect to given url and print the error code or the body
"""
import requests
import sys

if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    if html.status_code >= 400:
        print(f'Error code: {html.status_code}')
    else:
        print(html.text)
