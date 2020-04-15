#!/usr/bin/python3
"""
A script that takes your Github credentials (username and password) and
uses the Github API to display your id.
"""
import requests
from sys import argv


def run():
    """
    Displays github user ID.
    """
    un = argv[1]
    pw = argv[2]
    url = 'https://api.github.com/user'
    headers = {}
    headers['username'] = un
    headers['Authorization'] = 'token ' + pw
    r = requests.get(url, headers=headers)
    if (r.status_code == 200):
        j = r.json()
        print(j['id'])
    else:
        print('None')


if __name__ == "__main__":
    run()
