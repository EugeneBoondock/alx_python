import json, requests, sys

def get_employee_data(employee_id):
    # URL to fetch employee details for all employees
    employee_url = f"https://jsonplaceholder.typicode.com/users"
    
    try:
        # Fetch data for all employees
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        all_data = {}
        
        # Iterate over all employees
        for employee in employee_data:
            employee_id = employee["id"]
            employee_name = employee["name"]
            
            # Fetch to do list
            _, todos_data = fetch_todos(employee_id)
            
            # Extract completed tasks for the employee
            completed_tasks = [{"username": employee_name, "task": todo["title"], "completed": todo["completed"]} for todo in todos_data if todo["completed"]]
            
            all_data[employee_id] = completed_tasks
            
        return all_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
        
def fetch_todos(employee_id):
    # URL to fetch employee's to do list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return todos_data
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
def print_todo_list_progress(employee_id, employee_name, completed_count, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")        
# exports the data to JSON format
def export_to_json(data):
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)

# this block checks if the script is being run directly
# and takes the employee ID as a command line argument if that's the case
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    data = {}

    for id in range(1, employee_id + 1):
        id, employee_name, completed_count, total_tasks, completed_tasks = get_employee_data(id)
        employee_data = [{"username": employee_name, "task": task["title"], "completed": task["completed"]} for task in completed_tasks]
        data[str(id)] = employee_data

    export_to_json(data)
    print("Data exported to todo_all_employees.json")