from django.shortcuts import render
from .models import Playlist, Profile
import requests
import json
import base64

# Create your views here.
def playlist_index(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/playlist_index.html', {'playlists': playlists})

def playlist_view(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'music/playlist_view.html', {'playlist': playlist})

def profile_view(request):
    return render(request, 'music/profile.html')

#search artist
def search(request):
    b_token = get_token()
    print(b_token)
    headers = {
        'Authorization': f'Bearer {b_token}',
    }

    artist = requests.get('https://api.spotify.com/v1/search?q=jimi+hendrix&type=artist', headers=headers)
    r = artist.content
    artist_decode = json.loads(r.decode())
    print(artist_decode)

    return render(request, 'music/search.html', {'artist_data': artist_decode})


def get_token():
    string_bytes = b'7f6d69ae386b414099749fee14c7bfc2:2f94240e53604bada9dd9f1fcb3b5275'
    encoded_data = base64.b64encode(string_bytes)
    basic_value = str(encoded_data, 'utf-8')
    print(basic_value)

    headers = {
        'Authorization': f'Basic {basic_value}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    payload = {
        'grant_type': 'client_credentials'
    }

    res = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=payload)
    # Parses out token
    print(res.status_code)
    print(res.content)
    r = res.content
    res_decode = json.loads(r.decode())
    print(res_decode['access_token'])
    auth_token = res_decode['access_token']
    return auth_token
