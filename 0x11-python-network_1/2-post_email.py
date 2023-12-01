#!/usr/bin/python3
"""
connect to given url and print the value of the X-Request-Id 
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    values = {'email' : email}
    data = urllib.parse.urlencode(values)
    data = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print(html)
