from django.shortcuts import render
from .models import Playlist, Profile

# Create your views here.
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/playlist_list.html', {'playlists': playlists})
