#!/usr/bin/python3
"""
A script that takes in 3 strings and sends a search request to the Twitter API:
- The first argument must be the Consumer Key (API Key)
- The second argument must be the Consumer Secret (API Secret)
- The third argument must be the search string
"""
from sys import argv
import requests
import base64

consumer_key = argv[1]
consumer_secret = argv[2]
search_string = argv[3]
auth_value = 'OAuth oauth_consumer_key={}'.format(consumer_key)
'''
headers = {
    'authorization': auth_value,
    'oauth_nonce': "OAUTH_NONCE",
    'oauth_signature': "OAUTH_SIGNATURE",
    'oauth_signature_method': "HMAC-SHA1",
    'oauth_timestamp': "OAUTH_TIMESTAMP",
    'oauth_token': consumer_secret,
    'oauth_version': "1.0"
}
'''
key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
#url = 'https://api.twitter.com/1.1/search/tweets.json'
url = 'https://api.twitter.com/oauth2/token'
params = {
    'q': search_string,
}
r = requests.post(url, params=params, headers=headers)
print(r)
