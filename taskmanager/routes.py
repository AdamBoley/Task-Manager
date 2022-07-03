from flask import render_template
from taskmanager import app, db


@app.route("/")
def home():
    return render_template("base.html")


# up to here is the standard way to set up a Flask application
