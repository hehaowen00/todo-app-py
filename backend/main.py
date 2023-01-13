from flask import Flask
from db import conn, cursor
from auth import auth_blueprint
from list import list_blueprint
from todo import todo_blueprint


app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(list_blueprint)
app.register_blueprint(todo_blueprint)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    pass
