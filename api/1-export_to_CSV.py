#!/usr/bin/env python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and exports it to CSV.
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
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Prepare the CSV data
    csv_data = []
    for todo in todos:
        csv_data.append([user_id, user_name, str(todo['completed']), todo['title']])

    # Write the data to a CSV file
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"Employee {user_name} is done with tasks({done_tasks}/{total_tasks}).")
    print(f"Data exported to {filename}")
