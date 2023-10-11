#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

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

    total_tasks = len(todos)
    done_tasks = sum([1 for todo in todos if todo['completed']])

    print("Employee {} is done with tasks({}/{}):".format(user_name, done_tasks, total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t {}".format(todo['title']))
