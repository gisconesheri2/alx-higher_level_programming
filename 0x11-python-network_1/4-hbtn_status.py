#!/usr/bin/python3
"""
connect to https://alx-intranet.hbtn.io/status using requests
"""
import requests

if __name__ == "__main__":
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(html.text)}')
    print(f'\t- content: {html.text}')
