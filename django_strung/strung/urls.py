from django.urls import path
from . import views

urlpatterns = [
  path('', views.music_feed, name='strung-feed'),
  path('discover', views.discover, name='discover'),
  path('')
]