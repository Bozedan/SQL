from controller.user_controller import UserController
from flask import Flask, make_response, jsonify, Blueprint, request
from exceptions.exceptions import AlreadyExistsError

USER_REQUEST_API = Blueprint('request_user_api', __name__)

userController = UserController()

def get_blueprint():
    return USER_REQUEST_API

@USER_REQUEST_API.route('/registration', methods=['POST'])
def registration():
    request_data = request.get_json()
    try:
        login = request_data['login']
        password = request_data['password']
    except KeyError:
        return jsonify({'error': 'Invalid request body'}), 400
    try:
        userController.signupStudent(login, password)
    except AlreadyExistsError:
        return jsonify({'error': 'Login already exists'}), 403
    return jsonify({}), 200
