#!/usr/bin/python3
"""
    A Python script that, using this REST API, for a given employee ID
    returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = f'{url}/users/{user_id}'
    todos = f'{url}/todos?userId={user_id}'
    data = requests.get(user).json()
    user_todos = requests.get(todos).json()
    username = data.get('name')
    task_done = [task['title'] for task in user_todos if task['completed']]

    print(f'Employee {username} is done with tasks ({len(task_done)}/\
{len(user_todos)}):')

    for task in task_done:
        print(f'\t {task}')
