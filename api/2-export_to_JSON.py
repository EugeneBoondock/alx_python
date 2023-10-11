#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
exports data in JSON format.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    json_data = {
        "USER_ID": [
            {"task": todo['title'], "completed": todo['completed'], "username": user_name}
            for todo in todos
        ]
    }

    json_file_name = '{}.json'.format(user_id)

    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Data has been exported to {}.".format(json_file_name))
