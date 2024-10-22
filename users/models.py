from django.contrib.auth.models import AbstractUser
from django.db import models

from users.choices import RoleChoice


class Account(AbstractUser):
    role = models.CharField(max_length=32, choices=RoleChoice.choices)
