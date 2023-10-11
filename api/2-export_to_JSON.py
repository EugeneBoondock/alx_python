# Export data to JSON format
import json

def export_to_json(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data['name']
    
    # Get employee TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    
    # Prepare data for export
    export_data = []
    for task in todo_data:
        export_data.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })
    
    # Export data to JSON file
    json_file = f"{employee_id}.json"
    with open(json_file, 'w') as file:
        json.dump({ "USER_ID": export_data }, file)
    
    employee_id = int(input("Enter employee ID: "))
    export_to_json(employee_id)

employee_id = int(input("Enter employee ID: "))
export_to_json(employee_id)