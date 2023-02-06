#!/usr/bin/python3
"""
A script that starts a Flask web application:
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
    the text variable (replace underscore _ symbols with a space

"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A function that return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'C %s' % escape(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
