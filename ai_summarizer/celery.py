import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_summarizer.settings')

app = Celery('ai_summarizer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()