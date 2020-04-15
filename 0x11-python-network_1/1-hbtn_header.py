#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variablefound in the header of the response.
"""
from sys import argv
from urllib import request


def run():
    """
    Sends request to URL and displays X-REquest-Id values.
    """
    url = argv[1]
    with request.urlopen(url) as res:
        print(res.headers['X-Request-Id'])


if __name__ == "__main__":
    run()
