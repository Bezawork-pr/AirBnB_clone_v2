#!/usr/bin/python3
"""
A script that starts a Flask web application:
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”

"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A function that return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb():
    """A function that return HBNB"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
