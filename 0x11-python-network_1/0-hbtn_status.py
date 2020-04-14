#!/usr/bin/python3
"""
Contains a Python script that fetches https://intranet.hbtn.io/status.
"""
import urllib.request


url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as res:
    r = res.read()
    print('Body response:')
    print('\t- type:', type(r))
    print('\t- content:', r)
    print('\t- utf8 content:', r.decode('utf-8'))
