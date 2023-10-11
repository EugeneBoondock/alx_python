import csv
import requests
import sys

def fetch_user_and_todo_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json() if user_response.status_code == 200 else None
    todo_data = todo_response.json() if todo_response.status_code == 200 else []

    return user_data, todo_data

def export_to_csv(employee_id, user_data, todo_data):
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for task in todo_data:
            csv_writer.writerow([user_data['id'], user_data['username'], task['completed'], task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_user_and_todo_data(employee_id)

    if user_data:
        completed_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)

        print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")

        export_to_csv(employee_id, user_data, todo_data)
        print(f"Data exported to {employee_id}.csv")
    else:
        print("User not found.")
