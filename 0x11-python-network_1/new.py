#!/usr/bin/python3
import base64
from sys import argv
import requests
import json

client_key = argv[1]
client_secret = argv[2]
search = argv[3]


key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
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

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

params = {
    'q': search,
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

r = requests.get(search_url, headers=search_headers, params=params)
j = r.json()
#print(j)
#print(json.dumps(j, indent=4, sort_keys=True))

for s in j['statuses']:
    #for a in s:
        #print(a)
    print(json.dumps(s['user'], indent=4, sort_keys=True))
    print('***************************************************************************')

#print(json.dumps(j, indent=4, sort_keys=True))

#for s in j['statuses']:
#    tid = s['id']
#    tt = s['text']
#    tun = s['user']['name']
#    print('[{}] {} by {}'.format(tid, tt, tun))

#for x in j['statuses']:
#    print(x['id'])
#    print(x['text'] + '\n')
#    print(x['user']['name'])
    #print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
