import csv
import requests

def export_to_csv(user_id):
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        total_tasks = len(todos)
        done_tasks = sum([1 for todo in todos if todo['completed']])
        writer.writerow([user_id, user_name, done_tasks, total_tasks])
        for todo in todos:
            if todo['completed']:
                writer.writerow([user_id, user_name, 'True', todo['title']])
            else:
                writer.writerow([user_id, user_name, 'False', todo['title']])

if __name__ == '__main__':
    user_id = argv[1]
    export_to_csv(user_id)