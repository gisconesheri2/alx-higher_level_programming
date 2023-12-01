#!/usr/bin/python3
"""
connect to given url and post the email address
"""
import requests
import sys

if __name__ == "__main__":
    html = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(html.text)
