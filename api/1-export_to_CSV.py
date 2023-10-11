#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
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

    total_tasks = len(todos)
    done_tasks = sum([1 for todo in todos if todo['completed']])

    # Export data to CSV
    csv_filename = '{}.csv'.format(user_id)
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            csv_writer.writerow([user_id, user_name, str(todo['completed']), todo['title'])

    print("Employee {} is done with tasks({}/{}):".format(user_name, done_tasks, total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t {}".format(todo['title']))

    print("Data exported to {}.".format(csv_filename))
