#!/usr/bin/python3
"""
A script that starts a Flask web application:
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of
    the text variable (replace underscore _ symbols with a space
    /python/(<text>): display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space
    /number/<n>: display “n is a number” only if n is an integer

"""
from flask import Flask, escape, abort
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
def c(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'C %s' % escape(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return 'n is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
