import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///myapp.db"

CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379'
