# Register your models here.

from django.contrib import admin
from .models import *

admin.site.register(UserProfileObject)
admin.site.register(User)
admin.site.register(MyUserObject)