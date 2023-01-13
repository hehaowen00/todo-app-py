from flask import Blueprint, Flask

list_blueprint = Blueprint('list', __name__)


@list_blueprint.blueprint.route('/', methods=['GET'])
def get_todo():
    pass


@list_blueprint.blueprint.route('/', methods=['POST'])
def create_todo():
    pass


@list_blueprint.blueprint.route('/', methods=['PUT'])
def update_todo():
    pass


@list_blueprint.blueprint.route('/', methods=['DELETE'])
def delete_todo():
    pass
