from django.db import models

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

class Profile(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='profiles')
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
