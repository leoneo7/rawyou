from rest_framework import routers
from .views import EmotionViewSet, TrackViewSet


router = routers.DefaultRouter()
router.register(r'emotions', EmotionViewSet)
router.register(r'tracks', TrackViewSet)