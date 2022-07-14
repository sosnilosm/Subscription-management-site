from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom USER class"""
    email_verify = models.BooleanField(default=False)

    pass
