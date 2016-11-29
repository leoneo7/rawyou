from rest_framework import serializers
from .models import User, Emotion, Track


class UserSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('authorization_key', 'access_token')

    def get_access_token(self, obj):
        return obj.createAccessToken()


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'