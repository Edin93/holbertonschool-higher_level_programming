#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""
import urllib.parse
import urllib.request
from sys import argv

url = argv[1]
email = argv[2]
values = {
    'email': email
}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))
