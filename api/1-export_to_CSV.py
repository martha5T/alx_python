# import csv
# import requests
# import sys

# def export_employee_todo_progress_to_csv(employee_id):
#     """
#     Fetches an employee's TODO list, creates a CSV file, and writes the data.

#     Args:
#         employee_id (int): The ID of the employee for whom to fetch TODO list and create a CSV file.
#     """
#     # Fetch employee details
#     employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
#     employee_response = requests.get(employee_url)

#     if employee_response.status_code != 200:
#         print(f"Employee with ID {employee_id} not found.")
#         return

#     employee_data = employee_response.json()
#     employee_username = employee_data['username']

#     # Fetch employee's TODO list
#     todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
#     todos_response = requests.get(todos_url)

#     if todos_response.status_code != 200:
#         print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
#         return

#     todos_data = todos_response.json()

#     # Create CSV file and write data
#     csv_filename = f"{employee_id}.csv"
#     with open(csv_filename, mode='w', newline='') as csv_file:
#         writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, delimiter=',', quotechar='"', escapechar='\\')

#         # Write CSV header
#         writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

#         # Write task data
#         # without quotes
#         # for todo in todos_data:
#         #     csv_line = [employee_id, employee_username, str(todo["completed"]), todo["title"]]
#         #     writer.writerow(csv_line)

#         # With double quotes
#         for todo in todos_data:
#             csv_line = [employee_id, employee_username, str(todo["completed"]), todo["title"]]
#             writer.writerow(csv_line)

# if __name__ == "__main__":
#     employee_id = int(sys.argv[1])
#     export_employee_todo_progress_to_csv(employee_id)


import requests
import sys

def export_employee_todo_progress_to_csv(employee_id):
    """
    Fetches an employee's TODO list, creates a CSV file, and writes the data.

    Args:
        employee_id (int): The ID of the employee for whom to fetch TODO list and create a CSV file.
    """
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_data = employee_response.json()
    employee_username = employee_data['username']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Create CSV file and write data
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:

        # Write task data with values enclosed in double quotes
        for index, todo in enumerate(todos_data):
            csv_line = f'"{employee_id}","{employee_username}","{str(todo["completed"])}","{todo["title"]}"'
            if index < len(todos_data) - 1:  # Check if it's not the last iteration
                csv_line += '\n'
            csv_file.write(csv_line)

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todo_progress_to_csv(employee_id)