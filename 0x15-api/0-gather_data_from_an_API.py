#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress using a REST API.
"""

import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if user_response.status_code != 200 or todo_response.status_code != 200:
            print("Failed to fetch data from the API")
            return

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_name = user_data.get("name")
        total_tasks = len(todo_data)
        completed_tasks = [task for task in todo_data if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py employee_id")
        sys.exit(1)
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
