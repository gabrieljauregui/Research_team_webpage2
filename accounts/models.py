from django.db import models
from django.contrib.auth.models import AbstractUser

#sign up models.py


class MyUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    job = models.CharField(max_length=100, blank=True)
    educational_achievement = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    objectives = models.TextField(max_length=500, blank=True)

