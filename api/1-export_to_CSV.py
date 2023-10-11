import csv, requests, sys

def get_employee_data(employee_id):
    # URL to fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # URL to fetch employee TO DO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Fetch employee data
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        # Fetch employee TO DO list
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return employee_data,todos_data
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(employee_id, employee_name, todos_data):
    csv_filename = f"{employee_id}.csv"
    
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write the tasks data
        for todo in todos_data:
            csv_writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])
            
def employee_info(employee_id):
    employee_data, todos_data = get_employee_data(employee_id)
    
    # Extract employee information
    employee_name = employee_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    
    csv_filename = f"{employee_id}.csv"
    with open(f"{employee_id}.csv", "r") as f:
        pass
    # for todo in todos_data:
    #     if todo["completed"]:
    #         print(f"\t {title['title']}\n")
    
    # Export data to csv
    export_to_csv(employee_id, employee_name, todos_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    employee_info(employee_id)
