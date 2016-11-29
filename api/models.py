from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from datetime import datetime


class UserManager(BaseUserManager):
    def create_user(self, uuid, password=None, **extra_fields):
        user = self.model(uuid=uuid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uuid, password):
        return self.create_user(uuid, password)


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'uuid'
    objects = UserManager()

    class Meta:
        pass

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


# class Emotion(models.Model):
#     emotion_id = models.AutoField(primary_key=True)
#     emotion_name = models.CharField(max_length=10)
#
#     def __str__(self):
#         return u'%s' % (self.emotion_name)
#
#
# class Track(models.Model):
#     track_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User, related_name='tracks')
#     emotion_id = models.ForeignKey(Emotion, related_name='tracks')
#     start_time = models.DateTimeField(default=datetime.now)
#     end_time = models.DateTimeField(default=datetime.now)
#
#     def __str__(self):
#         return u'%s' % (self.track_id)
