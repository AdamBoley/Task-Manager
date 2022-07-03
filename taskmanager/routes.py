from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


# up to here is the standard way to set up a Flask application, except with home.html


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    # the above will query the database and return all records from the Categories table, sorting by category_name
    return render_template("categories.html", categories=categories)
    # in the return statement, the first categories is a variable name that can be used in the HTML file
    # the second categories is the categories variable in the function, which holds the list


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))  # takes user back to categories page
        # the string category_name refers to the input field in the add_category form 
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
    # in the return statement, the first categories is a variable name that can be used in the HTML file
    # the second category is the category variable in the function, which is the category to be edited


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

