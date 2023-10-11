import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} employee_id".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

# Fetching employee details
employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
employee_response = requests.get(employee_url)
employee_data = employee_response.json()
employee_name = employee_data["name"]

# Fetching employee's TODO list
todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

# Counting completed tasks
total_tasks = len(todo_data)
completed_tasks = sum(task["completed"] for task in todo_data)

# Displaying progress report
output = "Employee {} is done with tasks({}/{}):\n".format(employee_name, completed_tasks, total_tasks)
for task in todo_data:
    if task["completed"]:
        output += "\t{} {}\n".format("\t", task["title"])

# Print the output
print(output, end="")
