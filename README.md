

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
Try to implement a modal that holds the delete buttons on both the tasks and categories pages  - i.e. place the delete buttons inside modals, and have the delete buttons call that modal.
To get around the problem of modals requiring unique ids, use id="#modal-{{category.id}}" or id="#modal-{{task.id}}" to generate unique IDs using the database category table category_id and task table task_id columns
Specifically for the functionality to delete categories, warn users that all tasks assigned to that category will be deleted as well

Use emailJS to send notifications and updates when tasks are created, deleted, close to due date, etc



Note:
I was able to add functionality that displays tasks on the homepage using a Materialize collapsible list by myself, using code from the add_category function. I'm still not sure how this works


Note: 
When creating the task table in the taskmanager database, I misnamed the column that determines if a task is urgent as "id_urgent". It should be "is_urgent", but I currently do not have the knowledge to change column headers


Due dates rendered from the database are in the YYYY-MM-DD format as standard, which is unhelpful. 
The Jinja / Python strftime ( string from time ) directive has been used to render due dates in a more user-friendly fashion 
The Jinja for loop in the tasks page also uses the sort method to sort the tasks bu due date

When adding the edit_task functionality, I figured out 90% of what was needed


Deployment notes:
Heroku needs a file called `requirements.txt`
This tells Heroku what dependencies and packages are installed

Run `pip3 list`
This shows all of the packages installed in the workspace

The output can be transcribed to a requirements.txt file with:
`pip3 freeze --local > requirements.txt`

Heroku also needs a Procfile:
`echo web: python run.py > Procfile`
The echo command will add a blank line to the bottom of the Procfile. This can cause issues with deploying, so delete it


The postgres database that holds the task and category tables is hosted locally, so Heroku will not be able to use it

Heroku will therefore need a database of its own

On the resources tab, under add-ons, search for Heroku Postgres and add it

Under Settings, a new Config Var will be created - DATABASE_URL with an associate value

In the local env.py file there is a DB_URL key, with a value of the local postgres database

DATABASE_URL and DB_URL are two completely separate databases

All environment variables in the env.py file should be added to the Heroku Config Vars, except the DEVELOPMENT and DB_URL variables

A small conditional check in the `__init__.py` file needs to be added to specify which database to use. If "DEVELOPMENT" == "True", use DB_URL, else use DATABASE_URL


Connect to Heroku, set remote and push as normal

Then check Config Vars. If the DATABASE_URL starts with postgres, make modifications to the `__init__.py` file:
import re
The add changes from `__init__.py`

Add tables to Heroku database:
Heroku -> Activity -> More -> run console
`from taskmanager import db`
`db.create_all()`
`exit()`

The app is currently inoperative

To try:
In Heroku console, use `set_pg` command
Read - https://dev.to/lawrence_eagles/causes-of-heroku-h10-app-crashed-error-and-how-to-solve-them-3jnl
Remove PORT config var
