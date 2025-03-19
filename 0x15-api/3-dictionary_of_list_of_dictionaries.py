#!/usr/bin/python3
"""
Fetch and export task data in JSON format for all employees.
"""

import json
import requests

# Define the base URL for the REST API
base_url = "http://jsonplaceholder.typicode.com/"

# Fetch user information
users_response = requests.get(f"{base_url}users")
users = users_response.json()

# Create a dictionary to store user tasks and another for usernames
user_tasks = {}
usernames = {}

# Populate user dictionaries
for user in users:
    user_id = user["id"]
    user_tasks[user_id] = []
    usernames[user_id] = user["username"]

# Fetch tasks (TODO list)
todos_response = requests.get(f"{base_url}todos")
todos = todos_response.json()

# Correct task assignment to ensure accurate data mapping
for todo in todos:
    user_id = todo["userId"]  # Correctly identify the user ID
    task_info = {
        "task": todo["title"],
        "completed": todo["completed"],
        "username": usernames[user_id],
    }
    # Append task information to the corresponding user's list of tasks
    user_tasks[user_id].append(task_info)

# Save the output data to a JSON file
with open("todo_all_employees.json", 'w') as jsonfile:
    json.dump(user_tasks, jsonfile, indent=4)
