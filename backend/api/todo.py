from flask import Blueprint, Flask

todo_blueprint = Blueprint('todos', __name__)


@todo_blueprint.blueprint.route('/', methods=['GET'])
def get_todo():
    pass


@todo_blueprint.blueprint.route('/', methods=['POST'])
def create_todo():
    pass


@todo_blueprint.blueprint.route('/', methods=['PUT'])
def update_todo():
    pass


@todo_blueprint.blueprint.route('/', methods=['DELETE'])
def delete_todo():
    pass
