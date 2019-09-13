import os
from datetime import timedelta

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///myapp.db"

CELERY_BROKER_URL = 'redis://localhost:6379',
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

CELERYBEAT_SCHEDULE = {
        'run-every-1-minute': {
            'task':  'tasks.test.post_periodic_contacts',
            'schedule': timedelta(seconds=60)
        },
        # 'run-every-15-Secs': {
        #     #TODO --> Fill this 15 secs task
        #     'task':  "Second Task",
        #     'schedule': timedelta(seconds=15)
        # },
    }


