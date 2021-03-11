from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, CharField, IntegerField


class Achievement(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Upgrade(models.Model):
    name = CharField(max_length=128)
    cost = IntegerField(default=6969) # Noticeable default value to be overriden
    effect = IntegerField(default=1)
    auto_click = BooleanField(default=True)

    def  __str__(self):
        return self.name

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField()
    achievements = models.ManyToManyField(Achievement)
    upgrades = models.ManyToManyField(Upgrade)

    def __str__(self):
        return self.user.username