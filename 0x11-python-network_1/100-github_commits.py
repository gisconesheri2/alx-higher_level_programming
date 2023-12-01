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
    for l in resp_json[:10]:
        print(f"{l.get('sha')}: {l['commit']['author']['name']}")
