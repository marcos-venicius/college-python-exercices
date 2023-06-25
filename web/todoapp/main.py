"""
DISCLAIMER

I BUILT THIS CODE UNDER 10 MINUTES

PLEASE DO NOT USE THIS FOR PRODUCTION

THIS CODE IS NOT FOLLOWING ANY TYPE OF PATTERN OR BEST PRACTICES

THIS IS INSECURE AND NOT READY FOR PRODUCTION, USE THIS ONLY FOR TESTS PURPOSE ONLY.

THANK YOU.
"""

import uuid

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Todo:
    def __init__(self, identifier: str, name: str) -> None:
        self.id = identifier
        self.name = name


todos: dict[str, Todo] = {}


@app.route('/', methods=['GET'])
def render_list_todos():
    return render_template('index.html', todos_len=len(todos), todos=list(todos.values()))


@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.form['todo']

    if todo is None or todo.strip() == "":
        return "invalid todo name", 400

    iid = str(uuid.uuid4())

    todos[iid] = Todo(iid, todo.strip())

    return redirect('/', 302)


@app.route('/todos/<todo_id>', methods=['GET'])
def delete_todo(todo_id: str):
    global todos
    todos.pop(todo_id)
    return redirect('/', 302)


if __name__ == '__main__':
    app.run()
