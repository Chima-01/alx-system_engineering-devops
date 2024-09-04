#!/usr/bin/python3
"""
    extend your Python script to export data in the CSV format
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user = f'{url}/users'
    todos = f'{url}/todos'
    users = requests.get(user).json()
    tasks = requests.get(todos).json()
    id_username = [{"id": user['id'], "username": user['username']}
                   for user in users]

    total_employee_data = {}

    for user_data in id_username:
        new_list = []
        for task in tasks:
            if user_data.get('id') == task.get('userId'):
                todos_data = {"username": user_data.get('username'),
                              "task": task["title"],
                              "completed": task["completed"]}
                new_list.append(todos_data)
        total_employee_data[user_data.get('id')] = new_list

    with open(("todo_all_employees.json"), 'w') as f:
        json.dump(total_employee_data, f)

        f.close()
