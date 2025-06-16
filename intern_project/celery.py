import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intern_project.settings")

app = Celery("intern_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
