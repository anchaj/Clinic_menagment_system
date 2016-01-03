from __future__ import unicode_literals

from django.db import models
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.models import User
import re
import logging


# Create your models here.


class UserProfileObject(models.Model):
    pesel = models.CharField(max_length=11)
    first_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)


class LoginForm(forms.Form):
    username = forms.CharField(label="pesel", max_length=11)
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    def clean_pesel(self):
        logger = logging.getLogger('django')
        pesel = self.cleaned_data['pesel']
        logger.info("pesel: " + pesel)
        try:
            user = User.objects.get(username=pesel)
            return pesel
        except ObjectDoesNotExist:
            raise forms.ValidationError("Wrong password")

    def clean_password(self):
        logger = logging.getLogger('django')
        if 'pesel' in self.cleaned_data:
            pesel = self.cleaned_data['pesel']
            password = self.cleaned_data['password']
            logger.info("password: " + password)
            user = User.objects.get(username=pesel)
            if user.check_password(password):
                return password
            raise forms.ValidationError("Wrong password")
        raise forms.ValidationError("Wrong pesel")


class RegisterForm(forms.Form):
    pesel = forms.CharField(label="pesel")
    first_name = forms.CharField(label="first_name")
    surname = forms.CharField(label="surname")
    password = forms.CharField(label="password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="password2", widget=forms.PasswordInput())
    email = forms.EmailField(label="email")

    def clean_password2(self):
        logger = logging.getLogger('django')
        logger.info("clean_password2: " + str(self.cleaned_data))
        password = self.cleaned_data['password']
        logger.info("password: " + password)
        password2 = self.cleaned_data['password2']
        logger.info(" password2: " + password2)
        if password == password2:
            return password
        else:
            raise forms.ValidationError("Passwords not equal")

    """def clean_pesel(self):
        username = self.cleaned_data['pesel']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Bad characters in pesel")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("User already exist")"""
