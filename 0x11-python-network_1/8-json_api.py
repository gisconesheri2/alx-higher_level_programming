#!/usr/bin/python3
"""
connect to http://0.0.0.0:5000/search_user and send the supplied letter
get the response as JSON and print it
"""
import requests
import sys

if __name__ == "__main__":
    url  = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        values = {'q' : sys.argv[1]}
    else:
        values = {'q' : ""}

    html = requests.post(url, data=values)
    try:
        json_r = html.json()
        if len(json_r) == 0:
            print("No result")
        else:
            print(json_r)
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
    
