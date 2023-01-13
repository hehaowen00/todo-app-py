from flask import Blueprint, Flask

collection_blueprint = Blueprint('collection', __name__)


@collection_blueprint.blueprint.route('/', methods=['GET'])
def get_collection():
    pass


@collection_blueprint.blueprint.route('/', methods=['POST'])
def create_collection():
    pass


@collection_blueprint.blueprint.route('/', methods=['PUT'])
def update_collection():
    pass


@collection_blueprint.blueprint.route('/', methods=['DELETE'])
def delete_collection():
    pass
