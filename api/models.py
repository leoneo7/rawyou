from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Emotion(models.Model):
    emotion_name = models.CharField(max_length=10)

    def __str__(self):
        return u'%s' % (self.emotion_name)


class Track(models.Model):
    user = models.ForeignKey(User)
    emotion = models.ForeignKey(Emotion)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return u'%s' % (self.track_id)
