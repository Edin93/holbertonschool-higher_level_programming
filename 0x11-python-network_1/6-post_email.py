#!/usr/bin/python3
"""
A script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
from sys import argv


def run():
    """
    Sends a POST req to URL.
    """
    url = argv[1]
    email = argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    run()
