import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required

from task1.graphql.mutates import create_project_mutate, create_task_mutate
from task1.graphql.types import ProjectType, TaskType


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
        return CreateProject(task=task)


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_task = CreateTask.Field()


    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
