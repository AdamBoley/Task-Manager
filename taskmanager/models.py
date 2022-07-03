from taskmanager import db
# db contains each column type, which saves having to import each column type


class Category(db.Model):
    # the class-based model for various task categories in the application
    id = db.Column(db.Integer, primary_key=True)
    # id is the primary key, making each row unique 

    category_name = db.Column(db.String(30), unique=True, nullable=False)
    # category_name is the name of each category
    # db.string(30) means that values are strings with a maximum of 30 characters
    # unique=True means that each category entry must be unique. This prevents duplicate categories that might confuse things
    # nullable=False means that the field is required, sort of like how required can be added to a form input

    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    # note that this thing is db.relationship rather than db.Column
    # this means that it is defining a relationship, and this is linking the Category class to the Task Class

    def __repr__(self):
        # __repr__ means represent
        # represents class objects as strings
        # can also use the standard __str__ function
        return self.category_name


class Task(db.Model):
    # the class-based model for various individual tasks in the application
    id = db.Column(db.Integer, primary_key=True)

    task_name = db.Column(db.String(100), unique=True, nullable=False)

    task_description = db.Column(db.Text, nullable=False)
    # note that this column's data type is Text rather than String. Text allows for longer strings than String, much like how a textarea element allows longer inputs than a standard input element
    
    id_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # this column's datatype is Boolean, meaning that it can only hold values of true and false. The default value is false

    due_date = db.Column(db.Date, nullable=False)
    # this column's datatype is Date, meaning a date. Times can included with the DateTime or Time datatype

    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    # the ondelete keyword for this column sets how the tasks respond when the parent category is deleted. 
    # If the parent category is deleted, then all tasks with that category are also deleted, since each task must have a category assigned, per nullable=False

    def __repr__(self):
        # __repr__ means represent
        # represents class objects as strings
        # can also use the standard __str__ function
        return f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"






