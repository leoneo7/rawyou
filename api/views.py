import django_filters
from rest_framework import viewsets, filters, generics
from django.contrib.auth.models import User
from .models import Emotion, Track
from .serializer import UserSerializer, EmotionSerializer, TrackSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        queryset = Track.objects.all()
        user = self.request.user
        if str(user) is not "AnonymousUser":
            queryset = queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

