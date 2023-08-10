#!/usr/bin/python3
"""
This script takes the URL and sends request to the URL 
and it displays the value of the variable X-Request-Id.
"""
import requests
import sys

# Accept URL as a string argument
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the value of the X-Request-Id variable from the response header
    request_id = response.headers.get('X-Request-Id')
    # Print the value of X-Request-Id
    print(f"X-Request-Id: {request_id}")
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")