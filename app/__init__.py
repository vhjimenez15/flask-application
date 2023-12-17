from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# type enviroment
enviroment = config['development']

# Create FLask app
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


# Initialize db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# vistas
from app.elements.controllers import elementBp
from app.user.controllers import userBp
app.register_blueprint(elementBp)
app.register_blueprint(userBp)
