#!/usr/bin/python3
"""
A script that takes 2 arguments in order to solve this challenge:
- The first argument will be the repository name
- The second argument will be the owner name
to list 10 commits (from the most recent to oldest) of the repository's
given name by the user's given username.
"""
import requests
from sys import argv


def run():
    """
    Displays last 10 commits informations.
    """
    repo = argv[1]
    user = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    r = requests.get(url)
    commits = r.json()[:10]
    for c in commits:
        n = c.get('commit').get('author').get('name')
        sha = c.get('sha')
        print('{}: {}'.format(sha, n))


if __name__ == "__main__":
    run()
