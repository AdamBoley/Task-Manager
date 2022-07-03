

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


