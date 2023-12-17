from app import db
from flask import Blueprint, jsonify, request
# from flask_jwt_extended import jwt_required, get_jwt_identity
from app.user.uitls import create_token

from app.user.models import User, check_password

userBp = Blueprint('user', __name__)


@userBp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Query your database for username and password
    user = User.query.filter_by(username=username).first()
    if user is None and check_password(user.password, password):
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_token(user.id)
    return jsonify({ "token": access_token, "user": {"user_id": user.id, "username": user.username} })


# @userBp.route('/register', methods=['GET'])
# def register():
#     new_user = User('user1@gmail.com', 'username1', 'user1password', 'user1')
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify({'message': 'Successful'})
