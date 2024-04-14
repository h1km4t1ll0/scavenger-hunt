# celery.py
import os

from celery import Celery

from scavengerHunt import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scavengerHunt.settings')

# app = Celery('scavengerHunt')
app = Celery(__name__)
# app.config_from_object('scavengerHunt.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object(__name__)
# app.conf.broker_url = 'memory://'
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
