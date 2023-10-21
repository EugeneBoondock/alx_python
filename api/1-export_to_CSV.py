#!/usr/bin/python3
"""
Python script that exports data in the CSV format.
"""
import csv
import requests
from sys import argv

def export_data(user_id):
    """
    Request user info by employee ID.
    """
    try:
        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(user_id)).json()
        todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)).json()
    except requests.exceptions.RequestException as e:
        print("Something went wrong:", e)
        return

    username = user.get("username")

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            taskwriter.writerow([user_id, username, task['completed'], task['title']])

if __name__ == "__main__":
    if len(argv) > 1:
        export_data(argv[1])
