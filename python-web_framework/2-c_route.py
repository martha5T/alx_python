"""
This is a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL "/". Displays a greeting message.

    Returns:
    str: A string containing the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route handler for the root URL "/hbnb". Displays a string.

    Returns:
    str: A string containing the greeting message "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Route handler for the root URL "/c/<text>". Displays a string.

    Returns:
    str: A string containing the greeting message "C " + text.
    """
    return "C " + text.replace("_", " ")

if __name__ == "__main__":
    """
    Start the Flask web application.
    """
    app.run(host="0.0.0.0", port=5000)