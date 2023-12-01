#!/usr/bin/python3
"""
connect to given url and print the value of the X-Request-Id 
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = sys.argv[2]
    values = {'email' : data}
    email = urllib.parse.urlencode(values)
    email = email.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], email)

    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print(html.decode('utf-8'))
