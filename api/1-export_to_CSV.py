#!/usr/bin/python3
"""
    Python script that exports data in the CSV format
"""
import csv
import json
import requests
from sys import argv

def export_data(user_id):
    """
        Request user info by employee ID
    """
    try:
        request_employee = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
        request_employee.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        return
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
        return

    """
        Convert json to dictionary
    """
    user = json.loads(request_employee.text)
    """
        Extract username
    """
    username = user.get("username")

    """
        Request user's TODO list
    """
    try:
        request_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
        request_todos.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
        return
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return
    except requests.exceptions.RequestException as err:
        print ("Something went wrong",err)
        return

    """
        Dictionary to store task status(completed) in boolean format
    """
    tasks = {}
    """
        Convert json to list of dictionaries
    """
    user_todos = json.loads(request_todos.text)
    """
        Loop through dictionary & get completed tasks
    """
    for dictionary in user_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        Export to CSV
    """
    with open('{}.csv'.format(user_id), mode='w', newline='') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            file_editor.writerow([user_id, username, v, k])

if __name__ == "__main__":
   if len(argv) > 1:
       export_data(argv[1])
   else:
       print("Please provide a user id as an argument.")
