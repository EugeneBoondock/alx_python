import requests

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Get employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_data)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

employee_id = int(input("Enter employee ID: "))
get_employee_todo_progress(employee_id)
