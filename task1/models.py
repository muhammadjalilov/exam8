from django.db import models

from users.choices import StatusChoice
from users.models import Account


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='my_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    assignees = models.ManyToManyField(Account, related_name='projects')


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_tasks')
    status = models.CharField(max_length=32, choices=StatusChoice.choices,default=StatusChoice.DEVELOPMENT)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    assignees = models.ManyToManyField(Account, related_name='tasks')


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')

class Notification(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='notifications')
    message = models.TextField()
    type = models.CharField(max_length=32,)