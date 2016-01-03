from __future__ import unicode_literals

from django.db import models
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import logging
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=256)

    def check_password(self, text):
        logger = logging.getLogger('django')
        logging.info("check_password: " + text)
        return True

    def __str__(self):
        return "username: " + self.username + " password: " + self.password


class MyUserObject(models.Model):
    id = models.CharField(max_length=11, primary_key=True)
    first_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)


class UserProfileObject(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(MyUserObject, on_delete=models.CASCADE)


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    def clean_username(self):
        logger = logging.getLogger('django')
        username = self.cleaned_data['username']
        logger.info("username: " + username)
        try:
            user = User.objects.get(username=username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError("Wrong password")

    def clean_password(self):
        logger = logging.getLogger('django')
        if 'username' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            logger.info("password: " + password)
            user = User.objects.get(username=username)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Wrong password")
        raise forms.ValidationError("Wrong pesel")