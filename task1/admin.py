from django.contrib import admin

from task1.models import Project, Task, Comment, Notification

admin.site.register([Project, Task, Comment, Notification])
