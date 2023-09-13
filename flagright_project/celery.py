# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flagright_project.settings')

app = Celery('flagright_project')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks.py in each Django app
app.autodiscover_tasks(['youtubeapi_app'])

app.conf.broker_url = 'redis://redis:6379/0'

# Define the schedule for your demo task
app.conf.beat_schedule = {
    'demo-task': {
        'task': 'youtubeapi_app.tasks.fetching_youtube_vedio_data',
        'schedule': 10.0,  # Run every 10 seconds
    },
}
