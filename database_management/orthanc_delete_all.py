#!/usr/bin/python3

import sys
import requests
import json

user = sys.argv[1]
password = sys.argv[2]

session = requests.Session()
session.auth = (user, password)

r = session.get('http://169.228.56.133:8042/patients')
print(r)
print('\n')
rjson = r.json()

for pat in rjson:
    rpat = session.delete('http://169.228.56.133:8042/patients/' + pat)
    print(rpat)
    print('\n')
    print('-----------------------------------------------------------')
