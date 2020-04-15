#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header.
"""
import requests
from sys import argv


def run():
    """
    Send req to URL and displays X-Request-Id value.
    """
    url = argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])


if __name__ == "__main__":
    run()
