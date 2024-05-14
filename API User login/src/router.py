from flask import Blueprint, request, jsonify
from src.controller import create_user, login_by_name 

routers = Blueprint('routers', __name__)

@routers.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    
    res = create_user(data)
    
    print (res['message'] == 'OK')
    
    if res['message'] == 'OK':
        return jsonify(res), 201
    return jsonify(res), 409

@routers.route('/user/username', methods=['POST'])
def login_by_username():
    data = request.get_json()
    
    res = login_by_name(data)
    if res['message'] == 'Ok':
        return jsonify({'message': 'contraseña correcta'}), 200
    return jsonify(res), 409

