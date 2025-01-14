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

i = 0
for pat in rjson:
    rpat = session.get('http://169.228.56.133:8042/patients/' + pat)
    rpatjson = rpat.json()
    print(rpatjson)
    print('\n')
    studies = rpatjson['Studies']
    print(studies)
    print('\n')

    for stu in studies:
        get_string = 'http://169.228.56.133:8042/studies/' + stu + '/archive'
        print(get_string)
        print('\n')
        rarchive = session.get(get_string)
        fname = '/space/bil-syn01/1/cmig_bil/ccc/orthanc_downloads/' + str(i) + '_' + stu + '.zip'
        with open(fname, 'wb') as file:
            data = rarchive.content
            file.write(data)

        i = i + 1

    print('-----------------------------------------------------------')
