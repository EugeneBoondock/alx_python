import requests
import sys
import csv

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_data = requests.get(employee_url).json()
    user_id = employee_data['id']
    username = employee_data['username']
    
    # Fetch TODO list for the employee
    todos_url = f"{base_url}/users/{employee_id}/todos"
    todos_data = requests.get(todos_url).json()
    
    # Create a CSV file
    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write the task data to the CSV file
        for todo in todos_data:
            completed_status = "True" if todo['completed'] else "False"
            task_title = todo['title']
            csv_writer.writerow([user_id, username, completed_status, task_title])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_data(employee_id)
            print(f"Data exported to {employee_id}.csv")
        except ValueError:
            print("Please provide a valid employee ID (an integer).")
