import csv
import requests

def export_to_csv(employee_id):
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
    
    # Prepare data for CSV export
    csv_data = []
    for task in completed_tasks:
        csv_data.append([employee_id, employee_name, task['completed'], task['title']])
        
        # Export data to CSV file
    csv_file = f"{employee_id}_tasks.csv"
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(csv_data)
        
        employee_id = int(input("Enter employee ID: "))
        export_to_csv(employee_id)
