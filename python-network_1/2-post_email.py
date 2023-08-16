#!/usr/bin/python3
"""
This module takes in a url and an email
address, and posts the email to the url.
"""
import requests
import sys


if len(sys.argv) != 3:
    print("Usage: python script.py <url> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

response = requests.post(url, data={'email': email})
print(f"Your email is: {email}")
