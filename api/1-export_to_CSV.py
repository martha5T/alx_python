import requests
import sys

def get_employee_todo_progress(employee_id):
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
    employee_name = employee_data['name']

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

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print the employee's TODO list progress in the specified format
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Print the titles of completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
