from django.db import models
from datetime import datetime


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    authorization_key = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255, unique=True)

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
