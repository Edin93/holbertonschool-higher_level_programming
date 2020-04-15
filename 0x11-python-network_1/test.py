#!/usr/bin/python3
import requests
import base64
from sys import argv

#Define your keys from the developer portal
client_key = argv[1]
client_secret = argv[2]
search = argv[3]

#Reformat the keys and encode them

# we start in unicode and then transform to bytes
key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')


# Transform from bytes to bytes that can be printed
b64_encoded_key = base64.b64encode(key_secret)


#Transform from bytes back into Unicode
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}
params = {
    'q': search,
    'result_type': 'recent',
    'count': 5
}
r = requests.post(auth_url, headers=auth_headers, data=auth_data, params=params)
#r = requests.post(auth_url, headers=auth_headers)
print(r)
j = r.json()
print(r.content)