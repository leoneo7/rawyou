import django_filters
from rest_framework import viewsets, filters
from .models import User\
    # , Emotion, Track
from .serializer import UserSerializer\
    # ,EmotionSerializer, TrackSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class EmotionViewSet(viewsets.ModelViewSet):
#     queryset = Emotion.objects.all()
#     serializer_class = EmotionSerializer
#
#
# class TrackViewSet(viewsets.ModelViewSet):
#     queryset = Track.objects.all()
#     serializer_class = TrackSerializer