#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status.
"""
import requests


def run():
    """
    Fetches https://intranet.hbtn.io/status.
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type:', type(r.text))
    print('\t- content:', r.text)


if __name__ == "__main__":
    run()
