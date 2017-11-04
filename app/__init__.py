from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_socketio import SocketIO

# Create app and import config
app = Flask(__name__)
app.config.from_object('config')

# Function to setup celery with app context
def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

# Adding Celery, SqlAlchemy (not used), and SocketIO
celery = make_celery(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, message_queue='redis://localhost:6379')

# Some random magic that is required
from app import views