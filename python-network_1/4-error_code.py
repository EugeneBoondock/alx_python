#!/usr/bin/python3
"""
This module sends a request and
checks for error codes greater or = to 400
"""
import sys
import requests


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <url>")
    sys.exit(1)

url = sys.argv[1]


response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print("Regular request")
