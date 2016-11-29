from rest_framework.authtoken.models import Token
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.conf import settings
import random, string

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    authorization_key = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255, blank=True)

    @receiver(post_save, sender=settings.API_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def createAccessToken(self):
        return self.access_token.join([random.choice(string.ascii_letters + string.digits) for i in range(30)])

    def __str__(self):
        return u'%s' % (self.user_id)


class Emotion(models.Model):
    emotion_id = models.AutoField(primary_key=True)
    emotion_name = models.CharField(max_length=10)

    def __str__(self):
        return u'%s' % (self.emotion_name)


class Track(models.Model):
    track_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    emotion_id = models.ForeignKey(Emotion, related_name='tracks')
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return u'%s' % (self.track_id)
