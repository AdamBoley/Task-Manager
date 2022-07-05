import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get(""),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )

# up to here is the standard way to set up a Flask application
