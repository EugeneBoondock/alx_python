#!/usr/bin/python3
"""
This module fetches X-Request-id from a custom url
then prints it out
if there isn't any, then an exception is raised.
"""
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    custom_id = response.headers.get('X-Request-Id')
    print("{}".format(custom_id))

except Exception as e:
    print(f"An error occurred while trying to process {url}: {e}")
