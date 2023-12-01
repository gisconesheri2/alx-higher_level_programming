#!/usr/bin/python3
"""list 10 most recent commits of a repo
accepts the repo name and owner
"""

import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    headers = {}
    headers['Accept'] = 'application/vnd.github+json'
    resp = requests.get(url, headers=headers)
    resp_json = resp.json()
    for comm in resp_json[:10]:
        print(f"{comm.get('sha')}: {comm['commit']['author']['name']}")
