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
    first_name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

pesel_correct = re.compile(r'^[0-9]*$')


class LoginForm(forms.Form):
    username = forms.CharField(label="pesel", max_length=11)
    password = forms.CharField(label="password", widget=forms.PasswordInput())

    def clean_username(self):
        pesel = self.cleaned_data['username']
        """if len(pesel) != 11:
            raise forms.ValidationError("Wrong pesel length")
        elif not pesel_correct.match(pesel):
            raise forms.ValidationError("Pesel have unavailable chars")"""
        return pesel

    def clean_password(self):
        logger = logging.getLogger('django')
        if 'username' in self.cleaned_data:
            pesel = self.cleaned_data['username']
            password = self.cleaned_data['password']
            logger.info("password: " + password)
            user = User.objects.get(username=pesel)
            if user.check_password(password):
                logger.info("PASSWORD CORRECT in form")
                return password
            raise forms.ValidationError("Wrong password")
        raise forms.ValidationError("Wrong pesel")


class RegisterForm(forms.Form):
    username = forms.CharField(label="pesel")
    first_name = forms.CharField(label="first_name")
    surname = forms.CharField(label="surname")
    password = forms.CharField(label="password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="password (again)", widget=forms.PasswordInput())
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

    def clean_username(self):
        pesel = self.cleaned_data['username']
        """if len(pesel) != 11:
            raise forms.ValidationError("Wrong pesel length")
        elif not pesel_correct.match(pesel):
            raise forms.ValidationError("Pesel have unavailable chars")"""
        return pesel
