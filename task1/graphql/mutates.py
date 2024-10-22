from task1.models import Project, Task, Notification
from users.choices import MessageType
from users.models import Account


def create_project_mutate(info, name, description, assignees):
    account = info.context.user
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
    assignees = Account.objects.filter(id__in=assignees)

    task = Task(
        name=name,
        description=description,
        project=project,
        deadline=deadline
    )
    task.save()
    task.assignees.set(assignees)
    notes = []
    for i in assignees:
        notes = Notification(
            user=i,
            message="Task Created for you!",
            type=MessageType.FOR_DEV
        )
    Notification.objects.bulk_create(notes)
    return task
