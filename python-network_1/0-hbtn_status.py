#!/usr/bin/python3
"""
Script: network_status_checker.py
A simple script to check the status of a website using the 'requests' library.

Author: [Your Name]

Usage:
    Run this script using the command: python network_status_checker.py
"""


import requests

r = 'https://alu-intranet.hbtn.io/status'

try:
    response = requests.get(r)
    response.raise_for_status()

    print(f"Body response:\n")
    print("- type: {}".format(type(r)))
    print("content: {}".format(response.text))

except requests.exceptions.RequestException as e:
    print(f"An error occurred while trying to access {r}: {e}")
