#!/usr/bin/python3

"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def first_line(employee_id):
    """ Fetch user name """

    resp = requests.get(users_url).json()

    name = None
    for user in resp:
        if user['id'] == employee_id:
            name = user['name']

    filename = 'student_output'

    with open(filename, 'r') as f:
        first = f.readline().strip()

    if name in first:
        print(f"Employee {name}: OK")
    else:
        print(f"Employee {name}: Incorrect")


def todo_list_progress(employee_id):
    """ Display employee's TODO list progress """

    resp = requests.get(todos_url, params={'userId': employee_id}).json()

    total_tasks = len(resp)
    completed_tasks = [task for task in resp if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./main.py employee_id")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    first_line(employee_id)
    todo_list_progress(employee_id)
