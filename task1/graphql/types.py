from graphene_django import DjangoObjectType

from task1.models import Project, Task


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'assignees']

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = '__all__'