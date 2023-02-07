#!/usr/bin/python3
"""
web application must be listening on 0.0.0.0, port 5000
use storage for fetching data from the storage engine 
After each request you must remove the current SQLAlchemy Session:
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        LI tag: description of one State: <state.id>: <B><state.name></B>
"""
import models
from flask import Flask, escape, render_template
states = models.storage.all("State")
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def render(states):
    """Render HTML
    By fetching from 7-states_list.html
    """
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardownapp(exc):
    """Tear down current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
