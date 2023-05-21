#!/usr/bin/python3
"""
2-hello_route module.
a script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hnb():
    """starts a Flask web application
    Return:
        string:“Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hnb():
    """starts a Flask web application
    Adding specific route
    Return:
        string:“HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text=None):
    """starts a Flask web application
    Dynamic inputted text
    Return:
        string:“C” + formated text
        replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
