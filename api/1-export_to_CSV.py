#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, user_name, todo['completed'], todo['title']])
