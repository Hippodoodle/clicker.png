from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.conf import settings


class Achievement(models.Model):
    name = CharField(max_length=128, unique=True)
    description = CharField(max_length=256)
    condition = IntegerField(default=0)
    current_score_achievement = BooleanField(default=False)

    def __str__(self):
        return self.name


class Upgrade(models.Model):
    name = CharField(max_length=128)
    cost = IntegerField(default=6969)  # Noticeable default value to be overriden
    effect = IntegerField(default=1)
    auto_click = BooleanField(default=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = IntegerField(default=0)
    lifetime_points = IntegerField(default=0)
    achievements = models.ManyToManyField(Achievement, blank=True)
    upgrades = models.ManyToManyField(Upgrade, through="OwnsUpgrade")
    darkmode = BooleanField(default=False)
    image = models.ImageField(upload_to="uploads/", default="../static/images/logo.png")

    def __str__(self):
        return self.user.username


class OwnsUpgrade(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
