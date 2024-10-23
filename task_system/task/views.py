from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import System_Task
import json 
# Create your views here.

def Task_Create(request):
    if request.method=="POST":
        user=request.POST.get(request.user)
        title=request.POST.get('title')
        description=request.POST.get('description')
        deadline=request.POST.get('deadline')
        task=System_Task(user=user,
                         title=title,
                         description=description,
                         deadline=deadline,
                         )
        task.save()
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'task_notifications',{
                'type':'task_creations',
                'value':json.dumps({
                    "title": title,
                    "description": description,
                    "deadline": deadline
                })
            }
        )
        # return JsonResponse({"message": "Task created successfully"})
    
    return render(request, 'task/task_creations.html')

def Show_Task(request):
    tasks=System_Task.objects.all()
    context={'tasks':tasks}
    return render(request, 'task/display_task.html',context)