from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MyUserObject

admin.site.register(MyUserObject)

