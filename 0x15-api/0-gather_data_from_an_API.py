#!/usr/bin/python3
'''
This script retrieves information about an employee's TODO list progress.
It accepts an employee ID as an argument and displays the number of completed
tasks and the total number of tasks, along with the titles of completed tasks.
'''

import requests  # Library to make HTTP requests
from sys import argv  # Module to access command line arguments

# Ensure the script is being run as a standalone program
if __name__ == "__main__":
    # Base URL for the REST API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get the employee ID from command line arguments
    employee_id = argv[1]

    # Fetch user information from the API
    user_url = f"{base_url}users/{employee_id}"
    user = requests.get(user_url).json()

    # Fetch the TODO list for the user
    todos_url = f"{base_url}todos?userId={employee_id}"
    todos = requests.get(todos_url).json()

    # List of completed tasks
    completed_tasks = []

    # Total number of tasks
    total_tasks = len(todos)

    # Iterate through the tasks to identify completed ones
    for todo in todos:
        if todo.get("completed"):
            # Append the title of completed tasks to the list
            completed_tasks.append(todo.get("title"))

    # Prepare the output text for task completion status
    summary_text = "Employee {} is done with tasks({}/{}):"
    print(
            summary_text.format(
                user.get("name"),
                len(completed_tasks),
                total_tasks
                )
    )
    # Print the titles of completed tasks with a tab and space for indentation
    for task in completed_tasks:
        print("\t ", task)  # Adding a tab and space for indentation
