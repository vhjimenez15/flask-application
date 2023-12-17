from flask import Blueprint, jsonify

from app.user.models import User

userBp = Blueprint('user', __name__)

@userBp.route('/register', methods=('GET', 'POST'))
def register():
    return jsonify({'message': 'register'})