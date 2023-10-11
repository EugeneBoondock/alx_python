import requests
import json

def get_data(url):
    """
    Function to send a GET request to the specified URL and return the response in JSON format.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        dict: The response from the GET request in JSON format.
    """
    response = requests.get(url)
    return response.json()

def record_all_tasks():
    """
    Function to record all tasks from all employees. The tasks are fetched from a REST API and 
    stored in a dictionary. The dictionary is then written to a file named 'todo_all_employees.json'.
    """
    # Fetch all users
    users = get_data('https://jsonplaceholder.typicode.com/users')
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch all todos for the current user
        todos = get_data(f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')

        tasks = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks.append(task)

        all_tasks[user_id] = tasks

    # Write the tasks to a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)

record_all_tasks()
