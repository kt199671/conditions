from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Conditionクラス
class Condition(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=3, decimal_places=1, default=36.5)
    conditioning = models.BooleanField()
    content = models.TextField(max_length=1000, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    pub_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner) + ', ' + str(self.temperature) + ', ' \
               + str(self.conditioning) + ', ' + str(self.content) + ', ' + str(self.pub_date) + ', ' + str(self.pub_time)

    class Meta:
        ordering = ('-pub_date','-pub_time',)

