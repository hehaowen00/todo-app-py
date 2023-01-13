from flask import Blueprint, Flask

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.blueprint.route('/register', methods=['POST'])
def register():
    pass


@auth_blueprint.blueprint.route('/refresh', methods=['POST'])
def refresh():
    pass


@auth_blueprint.blueprint.route('/login', methods=['POST'])
def login():
    pass


@auth_blueprint.blueprint.route('/logout', methods=['POST'])
def logout():
    pass
