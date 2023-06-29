# Step 1: Set up the Flask Environment

# Create a new directory for your project and navigate to it in your terminal.
# Set up a virtual environment (optional but recommended):

# python -m venv venv

# Activate the virtual environment:
# On Windows:
# venv\Scripts\activate

# On macOS/Linux:
# source venv/bin/activate

# Install Flask:
# pip install flask

# Step 2: Create the Flask App
# Create a new Python file (e.g., app.py) and open it in a code editor.



from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask app:


app = Flask(__name__)

# Create a list to store the to-do items:

todo_list = []

# Define the app routes and their corresponding functions:

@app.route("/", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        todo = request.form.get("todo")
        todo_list.append(todo)
        return redirect(url_for("todo"))
    return render_template("index.html", todo_list=todo_list)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    todo_list.pop(index)
    return redirect(url_for("todo"))


# Create an HTML template file called index.html in a templates directory:
"""
html
Copy code
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="POST" action="{{ url_for('todo') }}">
        <input type="text" name="todo" placeholder="Add a task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for item in todo_list %}
        <li>
            {{ item }}
            <form method="POST" action="{{ url_for('delete', index=loop.index0) }}">
                <button type="submit">Delete</button>
            </form>
        </li>
        {% endfor %}
    </ul>
</body>
</html>
"""


# Step 3: Run the Flask App

# Save the file and run the Flask app in your terminal:

# On Windows:
# set FLASK_APP=app.py
# flask run

# On macOS/Linux:
# export FLASK_APP=app.py
# flask run

# Step 4: Access the To-Do List App

# Open a web browser and go to http://localhost:5000 to access the To-Do List app.
# You can add tasks by entering them in the input field and clicking the "Add" button. The tasks will be displayed as a list.
# To delete a task, click the "Delete" button next to the task.
