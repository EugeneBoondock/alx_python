#!/usr/bin/python3
"""
This module does multiple things
just read the code
"""
import sys
import requests


if len(sys.argv) != 2:
    print(f"No result")
    sys.exit(1)

url = 'http://0.0.0.0:5000/search_user'
q = sys.argv[1]

q = str(q)

data = {'q': q}

if len(q) != 1:
    sys.exit(1)

if q == 0:
    q=""

response = requests.post(url, data={'q': q})
id = response.headers.get('X-Request-Id')

try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response['id'], json_response['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
