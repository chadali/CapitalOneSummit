# Secret Key used for a lot of stuff in flask internals
SECRET_KEY = 'DJDI553JDkj87DFf8sf8Dfjdnng8DFJdfjdfsL42423waatj'
# Database Location n Settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Celery Settings
CELERY_BROKER_URL='redis://localhost:6379',
CELERY_RESULT_BACKEND='redis://localhost:6379'
CELERY_IMPORTS = ('app.tasks')
CELERYD_MAX_TASKS_PER_CHILD=1
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']