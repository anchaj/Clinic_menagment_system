# Register your models here.

from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.register(User)
