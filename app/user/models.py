from app import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(400))
    name = db.Column(db.String(100))

    def check_password(self, password):
        return generate_password_hash(self.password, password)
