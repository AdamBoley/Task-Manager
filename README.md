

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.



Task Manager application using Materialize CSS, Flask and SQL Alchemy

Install Flask, SQL Alchemy and psycopg2 together:
`pip3 install Flask-SQLAlchemy psycopg2`


Run the application using Flask:
`python3 run.py`

Note:
A standard Flask application requires: 
A run.py file in the main directory
A directory named after the repository
Within that, a templates folder containing an html file called base.html
Within the named directory, two files called `__init__.py` and `routes.py`
An env.py file in the main directory

Comments have been added to `run.py`,  `__init__.py` and `routes.py` to show this code, and this may be used as a boilerplate for future applications

Create taskmanager database in postgres:
`CREATE DATABASE taskmanager;`

Switch to taskmanager database:
`\c taskmanager`

Push Category and Task class to the postgres database to create tables within the taskmanager database:
access python interpreter:
`python3`
import table models:
`from taskmanager import db`
Create tables:
`db.create_all()`
exit th python interpreter:
`exit`



Prior to running a development server:
`set_pg` to set the postgres environment variable
then:
`python3 run.py` as normal



To try:
In categories.html:
Try to implement a modal that holds the delete button - i.e. place the delete button inside a modal, and have the card delete button call that modal
To get around the problem of modals requiring unique ids, use id="#modal-{{category.id}}" to generate unique IDs using the database category table id column

Use emailJS to send notifications and updates when tasks are created, deleted, close to due date, etc


