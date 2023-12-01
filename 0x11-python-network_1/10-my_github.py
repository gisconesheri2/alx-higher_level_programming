#!/usr/bin/python3
"""
connect to github api and get user id
accepts username and personal access token as inputs
"""
import requests
import sys

if __name__ == "__main__":
    url = f'https://api.github.com/users/{sys.argv[1]}'
    headers = {}
    headers['Accept'] = 'application/vnd.github+json'
    headers['Authorization'] = f'Bearer {sys.argv[2]}'
    html = requests.get(url, headers=headers)
    print(html.json().get('id'))
