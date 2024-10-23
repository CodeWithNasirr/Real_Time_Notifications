import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_system.settings')

app = Celery('task_system')
 
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(['task'])


# Celery Beat Schedule for checking deadlines every minute
app.conf.beat_schedule = {
    'check_task_deadlines': {
        'task': 'task.tasks.check_task_deadlines',
        'schedule': 60.0,  # Every minute
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')