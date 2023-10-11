import requests
import json

def export_to_json():
    # Get all employee IDs
    employee_ids_url = "https://jsonplaceholder.typicode.com/users"
    employee_ids_response = requests.get(employee_ids_url)
    employee_ids_data = employee_ids_response.json()
    employee_ids = [employee['id'] for employee in employee_ids_data]

    # Create dictionary to store all tasks
    all_tasks = {}

    # Iterate over each employee ID
    for employee_id in employee_ids:
        # Get employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_username = employee_data['username']

        # Get employee TODO list
        todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Create list to store tasks for current employee
        employee_tasks = []

        # Iterate over each task
        for task in todo_data:
            task_title = task['title']
            task_completed = task['completed']

            # Create dictionary for current task
            task_dict = {
                "username": employee_username,
                "task": task_title,
                "completed": task_completed
            }

            # Add task dictionary to employee tasks list
            employee_tasks.append(task_dict)

        # Add employee tasks list to all tasks dictionary
        all_tasks[employee_id] = employee_tasks

    # Export data to JSON file
    json_file = "todo_all_employees.json"
    with open(json_file, 'w') as file:
        json.dump(all_tasks, file)

export_to_json()
