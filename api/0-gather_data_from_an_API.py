import requests

def get_employee_todos(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return None

def display_todo_progress(todos):
    completed_todos = [todo for todo in todos if todo["completed"]]
    total_todos = len(todos)
    completed_todos_count = len(completed_todos)
    employee_name = get_employee_name(todos[0]["userId"])
    print(f"Employee {employee_name} is done with tasks({completed_todos_count}/{total_todos}):")
    for todo in completed_todos:
        print(f"\t{todo['title']}")

def get_employee_name(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["name"]
    else:
        print(f"Error: Unable to fetch data for employee {employee_id}")
        return None

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    todos = get_employee_todos(employee_id)
    if todos:
        display_todo_progress(todos)
    else:
        print("No data found for employee.")