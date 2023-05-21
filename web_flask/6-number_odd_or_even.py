#!/usr/bin/python3
"""
6-hello_route module.
a script that starts a Flask web application
"""
from flask import Flask, render_template
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text=None):
    """starts a Flask web application
    Dynamic inputted text
    Return:
        string:“C” + formated text
        replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """starts a Flask web application
    Dynamic inputted text
    Return:
        string:“Python” + formated text
        replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def n_number(n):
    """starts a Flask web application
    Dynamic inputted text
    Return:
        string:n is a number” only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_number_template(n):
    """starts a Flask web application
    Dynamic inputted text
    Return:
         display a HTML page only if n is an integer
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_or_odd(n):
    """starts a Flask web application
    Dynamic inputted text
    Return:
         display a HTML page only if n is an integer
         H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if (n % 2) == 0:
        num_type = "even"
    else:
        num_type = "odd"
    return render_template('6-number_odd_or_even.html', num=n,
                           number_type=num_type)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
