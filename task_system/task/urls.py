
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.task_list,name='Task_lists'),
    path('',views.Show_Task,name='task-deadline'),
    path('create',views.Task_Create,name='task-create'),
]
