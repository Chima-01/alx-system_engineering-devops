#!/usr/bin/python3
"""
    extend your Python script to export data in the CSV format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = f'{url}/users/{user_id}'
    todos = f'{url}/todos?userId={user_id}'
    username = requests.get(user).json().get('username')
    tasks = requests.get(todos).json()
    new_list = []

    for task in tasks:
        todos_data = {"task": task["title"], "completed": task["completed"],
                      "username": username}
        new_list.append(todos_data)

    new_dict = {user_id: new_list}
    with open((user_id + '.json'), 'w') as f:
        json.dump(new_dict, f)

        f.close()
