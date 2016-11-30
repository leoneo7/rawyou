import django_filters
from rest_framework import viewsets, filters
from .models import Emotion, Track
from .serializer import EmotionSerializer, TrackSerializer


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer