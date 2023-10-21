#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to a CSV file.
"""

import requests
import csv
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

    with open(f'{user_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos:
            writer.writerow([user_id, user_name, str(todo['completed']), todo['title']])

    print(f"Data has been exported to {user_id}.csv successfully.")
