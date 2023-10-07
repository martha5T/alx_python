import requests
import csv
import sys

def export_employee_todo_to_csv(employee_id):
    # Construct the URL for the employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    
    # Fetch employee details using an HTTP GET request
    employee_response = requests.get(employee_url)

    # Check if the employee exists (HTTP status code 200 indicates success)
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Parse the JSON response to obtain employee data
    employee_data = employee_response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Construct the URL for the employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Fetch the employee's TODO list using an HTTP GET request
    todos_response = requests.get(todos_url)

    # Check if the TODO list was successfully fetched
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return

    # Parse the JSON response to obtain the TODO list data
    todos_data = todos_response.json()

    # Create a CSV file for the employee's TODO list
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the TODO list data to the CSV file
        for todo in todos_data:
            task_completed_status = "Completed" if todo['completed'] else "Not Completed"
            csv_writer.writerow([user_id, username, task_completed_status, todo['title']])

    print(f"CSV file '{csv_filename}' has been created with TODO list data.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        export_employee_todo_to_csv(employee_id)
