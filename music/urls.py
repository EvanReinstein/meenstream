from django.urls import path
from .import views

urlpatterns = [
    path('', views.playlist_index, name='playlist_index'),
]
