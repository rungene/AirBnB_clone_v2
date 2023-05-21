#!/usr/bin/python3
"""
1-hello_route module.
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
    Adding a specific route /hnnb
    Return:
        string:“HBNB”
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
