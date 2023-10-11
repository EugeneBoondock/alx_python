#!/usr/bin/env python3

import csv
import requests
from sys import argv

def user_info(user_id):
    file_name = '{}.csv'.format(user_id)
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # do something with each row
            pass 

if __name__ == '__main__':

    user_id = argv[1]
    
    # Write CSV file
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    todos = response.json()

    file_name = '{}.csv'.format(user_id)
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        for todo in todos:
            row = [user_id, user_name, str(todo['completed']), todo['title']]
            writer.writerow(row)

    # Now read CSV file
    user_info(user_id)