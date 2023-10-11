#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
exports data in CSV format.
"""

import csv
import requests
from sys import argv

if __name__ == '__main':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    csv_file_name = '{}.csv'.format(user_id)

    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            task_completed = "True" if todo['completed'] else "False"
            csv_writer.writerow([user_id, user_name, task_completed, todo['title']])

    print("Data has been exported to {}.".format(csv_file_name))
