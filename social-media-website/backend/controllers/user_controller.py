from models import User
from utils.auth import hash_password
from flask import request, jsonify

def register_user():
    data = request.get_json()
    user = User(username=data['username'], password_hash=hash_password(data['password']))
    # More user registration logic...
    return jsonify({'message': 'User registered successfully'}), 201
