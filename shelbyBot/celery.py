# celery.py
import os

from celery import Celery

from shelbyBot import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shelbyBot.settings')

# app = Celery('shelbyBot')
app = Celery(__name__)
# app.config_from_object('shelbyBot.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object(__name__)
# app.conf.broker_url = 'memory://'
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
