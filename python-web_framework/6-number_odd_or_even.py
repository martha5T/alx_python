"""
This is a simple Flask web application.
"""

from flask import Flask, render_template

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


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Route handler for the root URL "/python/(<text>)". Displays a string.

    Returns:
    str: A string containing the greeting message "Python " + text.
    """
    return "Python " + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route handler for the root URL "/number/<n>". Displays a string.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route handler for the root URL "/number_template/<n>". Displays a string.
    """
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<n>')
def odd_or_even(n):
    """
    A route handler for the URL '/number_odd_or_even/<n>'.
    It returns an HTML page with an H1 tag containing "Number: is even|odd".

    Args:
        n (int): The value of the number
    
    Returns:
        str: HTML page with H1 tag.
    """
    try:
        n = int(n)
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', n=n, status='even')
        else:
            return render_template('6-number_odd_or_even.html', n=n, status='odd')
    except ValueError:
        return "404 Not Found", 404

if __name__ == "__main__":
    """
    Start the Flask web application.
    """
    app.run(host="0.0.0.0", port=5000)