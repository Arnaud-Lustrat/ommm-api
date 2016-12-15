from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.utils import timezone


# Models :
from django.contrib.auth.models import User


class Subscriptions(models.Model):
    wording = models.CharField(max_length=128)
    price = models.IntegerField(default=0)


class ValidatedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 'username' 'email' and 'password'
    relationship = models.CharField(null=True, max_length=128)
    housing = models.CharField(null=True, max_length=128)
    weight = models.IntegerField(default=0)
    card_number = models.CharField(null=True, max_length=128)
    date_subscribing = models.DateTimeField(null=True, editable=False)
    health_level = models.IntegerField(default=10)
    subscription = models.ForeignKey(Subscriptions, null=True)


class Tags(models.Model):
    wording = models.CharField(max_length=128)


class Types(models.Model):
    wording = models.CharField(max_length=128)
    animation_name = models.CharField(blank=True, null=True, max_length=255)


class Exercises(models.Model):
    source = models.CharField(blank=True, null=True, max_length=255)
    total_session_count = models.BigIntegerField(default=0)
    total_fav = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now(), editable=False)
    updated_at = models.DateTimeField(default=timezone.now())
    thumbnail = models.CharField(blank=True, null=True, max_length=255)
    title = models.CharField(blank=True, null=True, max_length=128)
    type = models.ForeignKey(Types, null=True, related_name='type_exercises')
    tag = models.ForeignKey(Tags, null=True, related_name='tag_exercises')
    exercise_favs = models.ManyToManyField(ValidatedUser, null=True, related_name='user_favs')


class Sessions(models.Model):
    users = models.ForeignKey(ValidatedUser, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True)
    heartbeat = models.IntegerField(null=True)
    feeling = models.IntegerField(null=True, blank=True)


# Token :
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
