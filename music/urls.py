from django.urls import path
from .import views

urlpatterns = [
    path('', views.playlist_index, name='playlist_index'),
    path('<int:playlist_id>', views.playlist_view, name='playlist_view'),
    path('profile/<username>', views.profile_view, name="profile_view"),
    path('playlist/delete/<int:playlist_id>', views.playlist_delete, name = 'delete_playlist'),
]
