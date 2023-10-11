"""
Python script that, using this REST API, for a given employee ID,
exports data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from command line arguments
    employee_id = sys.argv[1]
    
    # Send a GET request to the API to fetch the user data
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    
    # Send a GET request to the API to fetch the user's todos
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)).json()

    tasks = []
    
    # For each todo, create a new dictionary with task details and append it to tasks list
    for task in todos:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user.get('username')
        })

    # Open a new JSON file and write the tasks data into it
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump({employee_id: tasks}, json_file)
