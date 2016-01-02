from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class MyUserObject(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)


class RegisterObject(models.Model):
    login = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(MyUserObject, on_delete=models.CASCADE)
