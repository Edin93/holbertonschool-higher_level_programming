#!/usr/bin/python3
"""
Contains a Python script that fetches https://intranet.hbtn.io/status.
"""
from urllib import request


def run():
    """
    Fetches https://intranet.hbtn.io/status.
    """
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as res:
        r = res.read()
        print('Body response:')
        print('\t- type:', type(r))
        print('\t- content:', r)
        print('\t- utf8 content:', r.decode('utf-8'))


if __name__ == "__main__":
    run()
