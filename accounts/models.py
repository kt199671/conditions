
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, position, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username = username,
            position = position,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, position, password):
        user = self.create_user(
            username=username,
            position=position,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    position = models.CharField(max_length=20, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['position',]
