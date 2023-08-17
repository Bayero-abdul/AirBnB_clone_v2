#!/usr/bin/python3
""" a flask web app that listens on 0.0.0.0,
port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c_is(text):
    """Displays C <text>"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route("/python/<string:text>", strict_slashes=False)
def python_is(text="is cool"):
    """Python <text>"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an integer"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
