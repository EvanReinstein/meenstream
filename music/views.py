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

def search(request):
    b_token = get_token()
    print(b_token)
    headers = {
        'Authorization': f'Bearer {b_token}',
    }

    user_one = requests.get('https://api.spotify.com/v1/search?q=jimi+hendrix&type=artist', headers=headers)
    r = user_one.content
    user_decode = json.loads(r.decode())
    print(user_decode)

    return render(request, 'music/search.html', {'user_data': user_decode})


def get_token():
    string_bytes = b'ec0c6c26ad2b44398e60ed99edab8ed0:9315766205704431b20908cbae72e86e'
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
