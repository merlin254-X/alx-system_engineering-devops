#!/usr/bin/python3
"""
Exports all tasks from all employees in a specified JSON format
"""

import json
import requests

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Fetch all users
    users = requests.get(base_url + "users").json()

    # Initialize a dictionary to hold tasks for each user
    all_tasks = {}

    # Iterate over each user to fetch their tasks
    for user in users:
        user_id = str(user["id"])  # Convert user ID to string for the dictionary key
        username = user["username"]  # Get username for each user
        
        # Fetch all tasks for this user
        todos = requests.get(base_url + "todos?userId={}".format(user_id)).json()

        # Store tasks in the required format
        all_tasks[user_id] = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos
        ]

    # Write all tasks to a JSON file named "todo_all_employees.json"
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)

    print("Task data for all employees written to", json_filename)
