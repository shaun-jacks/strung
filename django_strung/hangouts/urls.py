from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create/', views.create_hangout, name='create-hangout'),
    path('hangout_list/', views.HangoutListView.as_view(), name='hangout_list'),
]