#!/usr/bin/python3
"""
connect to https://alx-intranet.hbtn.io/status using urllib
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        html = resp.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        headers = resp.info()
        if 'utf-8' in headers['Content-Type']:
            print('\t- utf8 content: OK')
