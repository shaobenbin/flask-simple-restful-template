# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user
from {{cookiecutter.app_name}}.conf.extensions import csrf_protect, login_manager
from {{cookiecutter.app_name}}.services import UserService
from {{cookiecutter.app_name}}.conf.utils import wrap_json_response
from {{cookiecutter.app_name}}.models import User


blueprint = Blueprint('public', __name__)
api_v1_blueprint = Blueprint('api_v1', __name__, url_prefix="/api/v1.0")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    print("load_user of user_id:{}".format(user_id))
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    return "HelloWorld"


@api_v1_blueprint.route("/login", methods=['POST'])
@csrf_protect.exempt
def login():
    request_data = request.get_json(force=True)
    username = request_data['username']
    password = request_data['password']
    user = UserService.auth(username, password)
    if user:
        login_user(user)
        return jsonify(wrap_json_response(1, {}))
    else:
        return jsonify(wrap_json_response(0, {}))


@api_v1_blueprint.route("/register", methods=['POST'])
@csrf_protect.exempt
def register():
    request_data = request.get_json()
    username = request_data['username']
    password = request_data['password']
    email = request_data['email']
    user = UserService.create(username=username, password=password, email=email)
    if user:
        return jsonify(wrap_json_response(1, {}))
    else:
        return jsonify(wrap_json_response(0, {}))


@api_v1_blueprint.route("/csrftest", methods=['POST'])
def csrftest():
    return 'success'


@api_v1_blueprint.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify(wrap_json_response(1, {}))


@api_v1_blueprint.route("/security/test", methods=['GET'])
@login_required
def security_test():
    callback = request.args.get('callback')
    if callback:
        return "{}('{}')".format(callback, "this is security content. well job!")
    else:
        return "this's security content. well job!"
