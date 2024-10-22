import graphene

from task1.graphql.types import ProjectType, TaskType
from task1.models import Project, Task


class Query(graphene.ObjectType):
    projects = graphene.List(ProjectType)
    tasks = graphene.List(TaskType)

    def resolve_projects(root, info, **kwargs):
        queryset = Project.objects.all()
        return queryset

    def resolve_tasks(root, info, **kwargs):
        queryset = Task.objects.all()
        return queryset
