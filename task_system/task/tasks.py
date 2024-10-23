from celery import shared_task
from channels.layers import get_channel_layer
from .models import System_Task
from asgiref.sync import async_to_sync
import json
from django.utils import timezone
import pytz
@shared_task
def check_task_deadlines():
    now=timezone.now()
    upcoming_task=System_Task.objects.filter(deadline__lte = now + timezone.timedelta(minutes=5),notified=False)
    channel_layer=get_channel_layer()
    ist_timezone = pytz.timezone('Asia/Kolkata')

    for task in upcoming_task:
        # Send notification
        deadline_ist=task.deadline.astimezone(ist_timezone)
        async_to_sync(channel_layer.group_send)(
            'task_notifications', {
                'type': 'task_deadline',
                'value': json.dumps({
                    "title": task.title,
                    "description": task.description,
                    "deadline": str(task.deadline_ist)
                })
            }
        )
        
        # Mark task as notified
        task.notified = True
        task.save()