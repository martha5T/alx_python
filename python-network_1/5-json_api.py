#!/usr/bin/python3
"""
This is a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    Args:
        letter (str): The letter to be sent in the parameter.

    Returns:
        str: The formatted response string.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    response = requests.post(url, data=payload)

    if response.headers.get('content-type') == 'application/json':
        try:
            data = response.json()
            if data:
                return f"[{data['id']}] {data['name']}"
            else:
                return "No result"
        except ValueError:
            return "Not a valid JSON"
    else:
        return "Not a valid JSON"

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response_string = search_user(letter)
    print(response_string)