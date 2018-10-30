from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your models here.
class Playlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlist")
    name = models.CharField(max_length=100)
    image = models.TextField()
    url = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])
    photo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user_id}'
