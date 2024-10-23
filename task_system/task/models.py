from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class System_Task(models.Model):
    task_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    deadline=models.DateTimeField()
    notified = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title