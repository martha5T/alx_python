"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
import requests
import sys

def get_user_id(username, password):
    """
    Uses the GitHub API to fetch the user id.

    Args:
        username (str): Your GitHub username.
        password (str): Your personal access token.

    Returns:
        int: The user id.

    Raises:
        requests.exceptions.RequestException: If an error occurs during the HTTP request.
    """
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    response.raise_for_status()

    user_data = response.json()
    user_id = user_data["id"]

    return user_id

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    try:
        user_id = get_user_id(username, password)
        print(f"{user_id}")
    except requests.exceptions.RequestException as e:
        print(None)