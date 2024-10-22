from django.db.models import TextChoices


class RoleChoice(TextChoices):
    MAINTAINER = 'maintainer', 'Maintainer'
    DEVELOPER = 'developer', 'Developer'


class StatusChoice(TextChoices):
    DEVELOPMENT = 'development', 'Development'
    REVIEW = 'review', 'Review'
    completed = 'completed', 'Completed'


class MessageType(TextChoices):
    FOR_DEV = 'for_developer', 'For Developer'
    FOR_MAIN = 'for_maintainer', 'For Maintainer'
