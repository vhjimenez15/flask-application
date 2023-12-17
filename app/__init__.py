from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from config import config
import json

# type enviroment
enviroment = config['development']

# Create FLask app
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


# Initialize db
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)


# vistas
from app.elements.controllers import elementBp
from app.user.controllers import userBp
app.register_blueprint(elementBp)
app.register_blueprint(userBp)
