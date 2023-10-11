import requests

def get_employee_todo_list_progress(employee_id):
  """Returns information about an employee's TODO list progress.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A string containing the employee's name, the number of completed tasks,
    the total number of tasks, and a list of the titles of completed tasks.
  """

  # Get the employee details.
  employee_details_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  employee_details_response = requests.get(employee_details_url)
  employee_details = employee_details_response.json()

  # Get the TODO list for the employee.
  employee_todo_list_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
  employee_todo_list_response = requests.get(employee_todo_list_url)
  employee_todo_list = employee_todo_list_response.json()

  # Calculate the number of completed tasks.
  number_of_completed_tasks = 0
  for task in employee_todo_list:
    if task["completed"]:
      number_of_completed_tasks += 1

  # Calculate the total number of tasks.
  total_number_of_tasks = len(employee_todo_list)

  # Get a list of the titles of completed tasks.
  completed_task_titles = []
  for task in employee_todo_list:
    if task["completed"]:
      completed_task_titles.append(task["title"])

  # Format the output string.
  output_string = f"Employee {employee_details['name']} is done with tasks({number_of_completed_tasks}/{total_number_of_tasks}):\n"
  for task_title in completed_task_titles:
    output_string += f"    {task_title}\n"

  return output_string


if __name__ == "__main__":
  # Get the employee ID from the user.
  employee_id = int(input("Enter the employee ID: "))

  # Get the employee's TODO list progress and display it to the user.
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)
  print(employee_todo_list_progress)
