from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weiboAPI.settings')

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 129600}  # 36 hour.
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Pacific/Auckland'
# CELERY_ENABLE_UTC = True

app = Celery('weibo_api',
             backend=CELERY_RESULT_BACKEND,
             broker=BROKER_URL,
             include=['location.tasks',],)
app.config_from_object('celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
