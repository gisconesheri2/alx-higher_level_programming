#!/usr/bin/python3
"""
connect to given url and print the value of the X-Request-Id 
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print(html)
