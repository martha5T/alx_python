"""
Export TODO Progress of All Employees to JSON

This script fetches TODO lists of all employees and creates a JSON file with the data.
The script generates a JSON file containing tasks for all employees in the desired format.

Usage:
    python script_name.py

Example:
    To export TODO progress of all employees:
    python script_name.py
"""

import json
import requests

def fetch_employee_todo_progress(employee_id):
    """
    Fetches an employee's TODO list.

    Args:
        employee_id (int): The ID of the employee for whom to fetch the TODO list.

    Returns:
        list: A list of TODO tasks for the specified employee.
    """
    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return []

    return todos_response.json()

def export_todo_all_employees_to_json():
    """
    Fetches TODO lists of all employees and creates a JSON file with the data.
    """
    all_employee_data = {}

    # Fetch TODO progress for all employees (assuming employee IDs are consecutive integers)
    for employee_id in range(1, 11):  # Assuming 10 employees with IDs from 1 to 10
        todos_data = fetch_employee_todo_progress(employee_id)
        
        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(employee_url)

        if employee_response.status_code == 200:
            employee_data = employee_response.json()
            employee_username = employee_data['username']

            # Create JSON data in the desired format for the current employee
            employee_json_data = {
                "username": employee_username,
                "tasks": [
                    {"task": todo["title"], "completed": todo["completed"]}
                    for todo in todos_data
                ]
            }

            # Add employee data to the all_employee_data dictionary
            all_employee_data[str(employee_id)] = employee_json_data

    # Create JSON file and write data for all employees
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)

if __name__ == "__main__":
    export_todo_all_employees_to_json()