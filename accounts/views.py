from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from music.models import Playlist, Profile


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home') ##Double check this functionality/correctness
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        #kenny left the back end validation to us...
        if len(first_name) < 2:
            raise ValidationError(_('Invalid Credentials'))
        if len(last_name) < 2:
            raise ValidationError(_('Invalid Credentials'))
        #Check if passwords match
        if password == password2:
        #check if user already exists
            if User.objects.filter(username=username).exists():
                return render(request, 'accounts/register.html', {'error': 'That username is already been registered.  Please try a different username, thank you.'})
            else:
                #check if email exists
                if User.objects.filter(email=email).exists():
                    return render(request, 'accounts/register.html', {'error': 'That email is already register, do you need a username/password reminder?'})
                else:
                    #register the user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()

                    # Create a playlist variable like user variable above
                    playlist = Playlist.objects.create(user=user)
                    playlist.save()

                    # Create a profile variable like user variable above
                    profile = Profile.objects.create(user=user, playlist=playlist)
                    profile.save()

                    # the two lines below will automatically log the user in and send them to their page.  In the uncommented code we are not loggin them in, rather sending them to the login to do it themselves...
                    auth.login(request, user)
                    return redirect('home')
                    # return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'error': 'Passwords do not match.'})

    else:
        return render(request, 'accounts/register.html')
