from flask import Blueprint, request, jsonify
from models.user import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json

    user = User(
        username=data['username'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User Registered'})
