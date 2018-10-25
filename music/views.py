from django.shortcuts import render
from .models import Playlist, Profile

# Create your views here.
def playlist_index(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/playlist_index.html', {'playlists': playlists})
