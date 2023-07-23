#!/usr/bin/python3
"""A flask app that displays list of states
in hbnb
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exc):
    """Closes the database current session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def list_state():
    """Displays list of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def state(id):
    """Displays a state and its cities"""
    states = storage.all(State).values()
    state = None

    for state_obj in states:
        if id == state_obj.id:
            state = state_obj

    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
