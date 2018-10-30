from django.shortcuts import render
from .models import Playlist, Profile
from django.contrib.auth.models import User
from django.http import HttpResponse
import requests
import json
import base64

# Create your views here.
def playlist_index(request):
    playlists = Playlist.objects.all()
    name = request.POST['artist-name']
    image = request.POST['artist-image']
    url = request.POST['external-url']

    playlist = playlists.create(user_id=request.user.id, name=name, image=image, url=url)


    # playlist = Playlist.objects.filter(user_id=request.user.id)
    # playlist.update(name=name, image=image, url=url)

    print('ARTIST FORM = ', name, image, url)
    return render(request, 'music/playlist_index.html', {'playlists': playlists, 'playlist': playlist})

def playlist_view(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'music/playlist_view.html', {'playlist': playlist})

# def profile_view(request, username):
#     user = User.objects.get(username=username)
#
#     return render(request, 'music/profile.html', {'user': user})

# Includes search functionality
def profile_view(request, username):
    user = User.objects.get(username=username)
    # playlists = Playlist.objects.filter(user_id=username)
    b_token = get_token()
    print(b_token)
    headers = {
        'Authorization': f'Bearer {b_token}',
    }
    q = request.GET.get('content')
    type = request.GET.get('type')
    print(q)
    print (type)
    artist = requests.get(f'https://api.spotify.com/v1/search?q={q}&type={type}', headers=headers)
    r = artist.content
    artist_decode = json.loads(r.decode())
    # artist_parse = json.loads(r.decode())
    # # Variables for save function
    # artist_name = artist_parse['artists']['items'][0]['name']
    # artist_img = artist_parse['artists']['items'][0]['images'][1]['url']
    # artist_link = artist_parse['artists']['items'][0]['external_urls']['spotify']
    #
    # print(artist_parse['artists']['items'][0]['external_urls']['spotify'])

    return render(request, 'music/profile.html', {'artist_data': artist_decode, 'user': user})


def artist_for_tracks():
    b_token = get_token()
    headers = {
        'Authorization': f'Bearer {b_token}',
    }
    artist = requests.get('https://api.spotify.com/v1/search?q=jimi+hendrix&type=artist', headers=headers)
    r = artist.content
    artist_decode = json.loads(r.decode())
    artist = artist_decode['artists']
    items = artist['items']
    artist_id = items['id']
    print(artist)
    print(items)
    print(artist_id)
    # for item in artist.items:
    #     artist_id = item.id
    # return artist_id

def artist_top_tracks(request):
    artist_id = artist_for_tracks()
    b_token = get_token()
    headers = {
        'Authorization': f'Bearer {b_token}',
    }
    top_tracks = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US', headers=headers)
    t = top_tracks.content
    top_tracks_decode = json.loads(t.decode())
    print(top_tracks_decode)
    return render(request, 'music/tracks.html', {'top_tracks': top_tracks_decode})

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


# def artist_save(request):
#     name = request.POST['artist-name']
#     image = request.POST['artist-image']
#     url = request.POST['external-url']
#
#     print('ARTIST FORM = ', name, image, url)
