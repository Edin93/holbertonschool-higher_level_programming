#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
from sys import argv


def run():
    url = argv[1]
    r = requests.get(url)
    if (r.code_status >= 400):
        print('Error code:', r.status_code)
    else:
        print(r.text)


if __name__ == "__main__":
    run()
