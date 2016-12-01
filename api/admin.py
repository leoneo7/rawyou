from django.contrib import admin
from .models import Emotion, Track


@admin.register(Emotion)
class Emotion(admin.ModelAdmin):
    pass

@admin.register(Track)
class Track(admin.ModelAdmin):
    pass
