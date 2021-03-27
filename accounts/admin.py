from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

admin.site.register(User)