#!/usr/bin/python3
"""A flask app that displays list of states
in hbnb
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    """Closes the database current session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_state():
    """Displays list of states"""
    all_states = storage.all(State)
    return render_template("7-states_list.html", all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
