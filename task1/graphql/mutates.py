from rest_framework.exceptions import ValidationError

from task1.models import Project, Task, Notification, Comment
from users.choices import MessageType
from users.models import Account


def create_project_mutate(info, name, description, assignees):
    account = info.context.user
    if account.role != 'maintainer':
        raise ValidationError("You do not have permissions for this action")

    assignees = Account.objects.filter(id__in=assignees)
    project = Project(
        name=name,
        description=description
    )
    project.owner = account
    project.save()
    project.assignees.set(assignees)
    return project


def create_task_mutate(info, name, description, project, deadline, assignees):
    account = info.context.user
    if account.role != 'maintainer':
        raise ValidationError("You do not have permissions for this action")

    assignees = Account.objects.filter(id__in=assignees)
    project = Project.objects.get(pk=project)
    task = Task(
        name=name,
        description=description,
        project=project,
        deadline=deadline
    )
    task.save()
    task.assignees.set(assignees)
    for i in assignees:
        Notification.objects.create(
            user=i,
            message="Task Created for you!",
            type=MessageType.FOR_DEV
        )
    return task


def create_comment_mutate(info, text, task: Task):
    account = info.context.user
    maintainer = task.project.owner
    comment = Comment.objects.create(
        text=text,
        task=task
    )
    comment.author = account
    comment.save()

    Notification.objects.create(
        user=maintainer,
        message="Comment in your task!",
        type=MessageType.FOR_MAIN
    )

    return comment
