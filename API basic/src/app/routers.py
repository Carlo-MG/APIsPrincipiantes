from flask import Blueprint, request, jsonify
from app.models import User
from app import db

bp = Blueprint('routers', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'username and email are required'}), 400

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201
