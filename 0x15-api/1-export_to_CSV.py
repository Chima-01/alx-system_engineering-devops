#!/usr/bin/python3
"""
    extend your Python script to export data in the CSV format
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = f'{url}/users/{user_id}'
    todos = f'{url}/todos?userId={user_id}'
    username = requests.get(user).json().get('username')
    tasks = requests.get(todos).json()

    with open((user_id + '.csv'), 'w') as f:
        output = csv.writer(f, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks:
            output.writerow([task['userId'], username, task['completed'],
                            task['title']])

    f.close()
