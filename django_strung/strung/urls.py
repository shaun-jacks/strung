from django.urls import path
from . import views
from hangouts import views as hangout_views

urlpatterns = [
  path('', hangout_views.HangoutListView.as_view(), name='music_feed'),
  path('discover', views.discover, name='discover'),
]