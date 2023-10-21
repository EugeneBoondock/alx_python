#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import json
import requests
import sys


def check_user_id_type(student_json, user_id):
    student_dicts = student_json[user_id]
    if isinstance(student_dicts, list) and all(isinstance(item, dict) for item in student_dicts):
        print("USER_ID's value type is a list of dicts: OK")
    else:
        print("USER_ID's value type incorrect")


def check_all_tasks(student_json, user_id):
    if all("task" in item and "completed" in item and "username" in item for item in student_json[user_id]):
        print("All tasks found: OK")
    else:
        print("All tasks not found")


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    username = user.get('username')

    data = []

    for todo in todos:
        data.append({'task': todo.get('title'),
                     'completed': todo.get('completed'), 'username': username})

    student_dict = {user_id: data}

    filename = user_id + ".json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(student_dict, json_file, indent=2)

    with open(filename, 'r') as f:
        student_json = json.load(f)

    check_user_id_type(student_json, user_id)
    check_all_tasks(student_json, user_id)
