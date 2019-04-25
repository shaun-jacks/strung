from django.urls import path
from . import views

urlpatterns = [
  path('', views.music_feed, name='music_feed'),
  path('discover', views.discover, name='discover'),
]