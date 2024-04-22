#!/usr/bin/python3
"""
For a given employee ID, export all tasks owned by this employee in JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user and TODO data
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos?userId={}".format(employee_id)).json()

    # Structure the data as required
    tasks = {
        employee_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            for todo in todos
        ]
    }

    # Write to a JSON file with the employee ID as the filename
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump(tasks, jsonfile, indent=4)

    print("Task data written to", json_filename)
