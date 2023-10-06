import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Format and return progress as a string
    progress = "Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks)
    
    completed_task_titles = [todo['title'] for todo in todos_data if todo['completed']]
    progress += '\n' + '\n'.join(["\t " + title for title in completed_task_titles])

    return progress

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    progress = get_employee_todo_progress(employee_id)
    
    # Print the progress string to standard output
    print(progress)