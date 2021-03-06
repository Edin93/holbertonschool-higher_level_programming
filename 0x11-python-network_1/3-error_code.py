#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib import request, error


def run():
    """
    Sends a req to URL and displays resp body.
    """
    url = argv[1]
    try:
        with request.urlopen(url) as res:
            r = res.read()
            print(r.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == "__main__":
    run()
