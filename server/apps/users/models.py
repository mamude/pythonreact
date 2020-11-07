from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.core.models import AbstractBaseModel


class User(AbstractUser):
    token = models.CharField(max_length=255)
