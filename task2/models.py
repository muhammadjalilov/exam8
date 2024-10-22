from django.db import models

from users.models import Account


class LoggedInUser(models.Model):
    user = models.OneToOneField(Account, related_name='logged_in_user',on_delete=models.CASCADE)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username
