from rest_framework import routers
from .views import UserViewSet\
    # , EmotionViewSet, TrackViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'emotions', EmotionViewSet)
# router.register(r'tracks', TrackViewSet)