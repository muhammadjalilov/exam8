import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from rest_framework.exceptions import ValidationError

from task1.graphql.mutates import create_project_mutate, create_task_mutate, create_comment_mutate
from task1.graphql.types import ProjectType, TaskType, CommentType
from task1.models import Task
from users.models import Account


class CreateProject(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        assignees = graphene.List(graphene.ID)

    project = graphene.Field(ProjectType)

    @classmethod
    @login_required
    def mutate(cls, root, info, name, description, assignees):
        project = create_project_mutate(info, name, description, assignees)
        return CreateProject(project=project)


class CreateTask(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        project = graphene.Int(required=True)
        deadline = graphene.DateTime(required=True)
        assignees = graphene.List(graphene.ID)

    task = graphene.Field(TaskType)

    @classmethod
    @login_required
    def mutate(cls, root, info, name, description, project, deadline, assignees):
        task = create_task_mutate(info, name, description, project, deadline, assignees)
        return CreateTask(task=task)


class UpdateTask(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        status = graphene.String()

    task = graphene.Field(TaskType)

    @classmethod
    @login_required
    def mutate(cls, root, info, id, status):
        user: Account = info.context.user
        task: Task = Task.objects.filter(pk=id).first()
        if not task.assignees.filter(id=id):
            raise ValidationError("You cannot change this task!")

        task.status = status
        task.save()
        return UpdateTask(task=task)


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        task = graphene.ID(required=True)

    comment = graphene.Field(CommentType)

    @classmethod
    @login_required
    def mutate(cls, root, info, text, task):
        project = create_comment_mutate(info, text, task)
        return CreateComment(project=project)


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_task = CreateTask.Field()
    update_task = UpdateTask.Field()
    create_comment = CreateComment.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
