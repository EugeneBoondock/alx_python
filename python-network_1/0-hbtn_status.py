#!/usr/bin/python3
"""
Sends request to alu website
"""
import requests


r = requests.get('https://alu-intranet.hbtn.io/status')
print(requests.text)
