#!/usr/bin/python3

# getcve.py
#
# The quick and dirty CVE information retrieval script
# BY:   Doug Leidgen


import requests
import sys
import json

# Kill off any SSL warnings issued by requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


if sys.argv[1] == '-h':
    print('Usage:  getcve [CVE ID]')
else:
    cveid = str(sys.argv[1])


url = 'https://cve.circl.lu/api/cve/' + cveid

# Get JSON
consume = requests.get(url)
# Convert JSON to dict
payload = consume.json()

print('\nID: ', payload['id'])
print('Published: ', payload['Published'])
print('CVSS Score: ', payload['cvss'])
print('Impact: ', payload['impact'])
print('\nSummary: ', payload['summary'])
print(' ')

sys.exit()
