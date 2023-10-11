import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Construct the URLs for employee details and their TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"
    
    # Send requests to get employee details and their TODO list
    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)
    
    # Check if the requests were successful
    if employee_response.status_code != 200 or todo_response.status_code != 200:
        print("Failed to fetch data from the API.")
        return
    
    # Parse JSON data
    employee_data = employee_response.json()
    todo_data = todo_response.json()
    
    # Extract employee information
    employee_name = employee_data.get("name")
    
    # Count the number of completed and total tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])
    
    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
