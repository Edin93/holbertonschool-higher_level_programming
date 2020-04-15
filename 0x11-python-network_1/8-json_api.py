#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


def run():
    """
    Sends a POST req to the URL.
    """
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        j = r.json()
        if bool(j):
            print('[{}] {}'.format(j['id'], j['name']))
        else:
            print('No result')
    except ValueError as e:
        print('Not a valid JSON')


if __name__ == "__main__":
    run()
