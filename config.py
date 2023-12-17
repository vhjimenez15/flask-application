import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = "mysql+pymysql://root:password_mysql@db/db_mysql"


class BaseConfig:
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    PROPAGATE_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
}
