#pip install requests
#pip install requests_oauthlib

# to include installing within the code https://stackoverflow.com/questions/12332975/installing-python-module-within-code

import requests
from requests_oauthlib import OAuth1
import json

api_key = 'te7aObJVJRG47oqfElsFFxtiM'
api_secret = 'JlG2S7NGrbFdBQCUODTaMxXPo5ya3BXVuOoy83PsXrrFWLXzsT'
access_token_key = '925739571127529472-NceiRZ6cgVxmGngPTQQ7LApFXJSo5l6'
access_token_secret = 'km6P0PRgFqKMO9T1znlRqBDcCGUiBvTwolwUgdRRGTagv'

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(api_key, api_secret, access_token_key, access_token_secret)

url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
#print(r.status_code)

if r.encoding is None:
    r.encoding = 'utf-8'
for line in r.iter_lines(decode_unicode=True):
    print(json.dumps(line), "\n")


url = 'https://stream.twitter.com/1.1/statuses/sample.json'
r = requests.get(url, auth=auth, stream=True)
if r.encoding is None:
    r.encoding = 'utf-8'

with open('req_output.json', 'w') as ofile:
    for line in r.iter_lines(decode_unicode=True):
        if line:
            ofile.write(json.dumps(line))
            ofile.write('\n')
