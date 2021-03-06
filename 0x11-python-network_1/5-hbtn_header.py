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
    try:
        r = requests.get(url)
        print(r.headers.get('X-Request-Id'))
    except requests.exceptions.ConnectionError as e:
        pass


if __name__ == "__main__":
    run()
