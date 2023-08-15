#!/usr/bin/python3
"""
This module fetches X-Request-id from a custom url
then prints it out
if there isn't any, then an exception is raised.
"""
import requests, sys


url = 'https://www.earth2.io'

try:
    custom_id = url.headers.get('X-Request-Id')
    print(custom_id)

except Exception as e:
    print(f"An error occurred while trying to process {r}: {e}")
