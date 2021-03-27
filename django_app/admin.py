from django.contrib import admin
from condition.models import Condition
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


admin.site.register(Condition)
admin.site.register(User)