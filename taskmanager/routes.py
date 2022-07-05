from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())

    return render_template("tasks.html", tasks=tasks)


# up to here is the standard way to set up a Flask application,
# except with home.html instead of tasks.html


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


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    # categories variable is required because we need to assign each task to a category before it can be created, so we need a list of categories we can used
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            id_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add_task.html", categories=categories)
    # in the return statement, the first categories is a variable name that can be used in the HTML file
    # the second category is the category variable in the function, which is the category to be edited


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":
        
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.id_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        
        db.session.commit()

    return render_template("edit_task.html", task=task, categories=categories)





