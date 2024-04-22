#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
"""

import csv
import requests
from sys import argv

# Base URL for the API
url = 'https://jsonplaceholder.typicode.com/'

# Ensure we have the correct number of arguments
if len(argv) != 2:
    print("Usage: {} <employee_id>".format(argv[0]))
    exit(1)

# Get the employee ID from command-line arguments
employee_id = argv[1]

try:
    # Fetch user data
    user = requests.get(url + "users/{}".format(employee_id)).json()
    if 'username' not in user:
        print("User with ID {} not found.".format(employee_id))
        exit(1)

    # Fetch TODO list for the given user
    todos = requests.get(url + "todos?userId={}".format(employee_id)).json()

    # Create CSV file with the employee ID as the filename
    with open('{}.csv'.format(employee_id), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write data to the CSV file
        for todo in todos:
            my_writer.writerow([
                employee_id,          # User ID
                user.get('username'),  # Username
                todo.get('completed'),  # Task completion status
                todo.get('title')      # Task title
            ])

    print("TODO list data written to {}.csv".format(employee_id))

except requests.RequestException as e:
    print("An error occurred while fetching data:", e)
    exit(1)
