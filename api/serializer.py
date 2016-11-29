from rest_framework import serializers
from .models import User\
    # , Emotion, Track


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class EmotionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Emotion
#         fields = '__all__'
#
#
# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = '__all__'