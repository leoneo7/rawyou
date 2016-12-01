from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Emotion, Track


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('emotion_name',)


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('emotion', 'start_time', 'end_time')